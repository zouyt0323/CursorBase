"""Lark/Feishu API client with WebSocket long connection for real-time messaging."""

import json
import time
import logging
import threading
from queue import Queue, Empty
from typing import Optional

import lark_oapi as lark
from lark_oapi.api.im.v1 import (
    CreateMessageRequest,
    CreateMessageRequestBody,
    CreateMessageResponse,
    ListMessageRequest,
    ListMessageResponse,
    P2ImMessageReceiveV1,
)

logger = logging.getLogger(__name__)


class LarkClient:
    """Wraps Lark SDK with WebSocket long connection for real-time message receiving."""

    def __init__(self, app_id: str, app_secret: str, chat_id: str,
                 encrypt_key: str = "", verification_token: str = ""):
        self._app_id = app_id
        self._app_secret = app_secret
        self._chat_id = chat_id
        self._encrypt_key = encrypt_key
        self._verification_token = verification_token
        self._client = lark.Client.builder() \
            .app_id(app_id) \
            .app_secret(app_secret) \
            .log_level(lark.LogLevel.WARNING) \
            .build()
        self._msg_queue: Queue = Queue()
        self._ws_connected = False
        self._ws_client = None
        self._start_websocket()

    def _start_websocket(self):
        """Start WebSocket long connection in a background thread."""
        try:
            handler = lark.EventDispatcherHandler.builder(
                self._encrypt_key, self._verification_token
            ).register_p2_im_message_receive_v1(self._on_message_receive) \
                .build()

            self._ws_client = lark.ws.Client(
                app_id=self._app_id,
                app_secret=self._app_secret,
                event_handler=handler,
                log_level=lark.LogLevel.WARNING,
                auto_reconnect=True,
            )

            thread = threading.Thread(target=self._run_ws, daemon=True)
            thread.start()
            logger.info("WebSocket connection starting in background thread")
        except Exception as exc:
            logger.warning("Failed to start WebSocket, falling back to polling: %s", exc)

    def _run_ws(self):
        """Run WebSocket client (blocking, runs in daemon thread)."""
        try:
            self._ws_connected = True
            self._ws_client.start()
        except Exception as exc:
            logger.error("WebSocket connection error: %s", exc)
            self._ws_connected = False

    def _on_message_receive(self, data: P2ImMessageReceiveV1):
        """Handle incoming message events from WebSocket (group chat only)."""
        try:
            msg = data.event.message
            sender = data.event.sender

            if not msg or not sender:
                return

            event_chat_id = getattr(msg, "chat_id", "")
            if event_chat_id != self._chat_id:
                return

            sender_type = getattr(getattr(sender, "sender_type", None), "value", "")
            if not sender_type:
                sender_type = str(getattr(sender, "sender_type", ""))

            if "app" in sender_type.lower():
                return

            msg_type = getattr(msg, "message_type", "")
            if msg_type != "text":
                return

            content_str = getattr(msg, "content", "{}")
            content = json.loads(content_str)
            text = content.get("text", "")

            if text:
                self._msg_queue.put(text)
                logger.info("WebSocket received message: %s", text[:50])
        except Exception as exc:
            logger.warning("Error processing WebSocket message: %s", exc)

    def send_message(self, text: str) -> bool:
        """Send a text message to the configured group chat."""
        content = json.dumps({"text": text}, ensure_ascii=False)
        req = CreateMessageRequest.builder() \
            .receive_id_type("chat_id") \
            .request_body(
                CreateMessageRequestBody.builder()
                .receive_id(self._chat_id)
                .msg_type("text")
                .content(content)
                .build()
            ).build()

        resp: CreateMessageResponse = self._client.im.v1.message.create(req)
        if not resp.success():
            logger.error("send_message failed: code=%s msg=%s", resp.code, resp.msg)
            return False

        return True

    def poll_user_message(
        self,
        timeout: int = 600,
        interval: float = 3.0,
    ) -> Optional[str]:
        """Wait for a new user message.

        If WebSocket is connected, waits on the message queue (real-time).
        Otherwise falls back to API polling.
        """
        self._msg_queue = Queue()

        if self._ws_connected:
            return self._wait_from_queue(timeout)

        return self._poll_from_api(timeout, interval)

    def _wait_from_queue(self, timeout: int) -> Optional[str]:
        """Wait for a message from the WebSocket queue."""
        try:
            text = self._msg_queue.get(timeout=timeout)
            return text
        except Empty:
            return None

    def _poll_from_api(self, timeout: int, interval: float) -> Optional[str]:
        """Fallback: poll the API for new messages."""
        deadline = time.time() + timeout
        baseline_ts = str(int(time.time() * 1000))

        while time.time() < deadline:
            try:
                text = self._fetch_latest_user_message(baseline_ts)
                if text is not None:
                    return text
            except Exception as exc:
                logger.warning("poll error: %s", exc)
            time.sleep(interval)

        return None

    def _fetch_latest_user_message(self, since_ts: str) -> Optional[str]:
        """Fetch recent messages and return the newest user message after since_ts."""
        req = ListMessageRequest.builder() \
            .container_id_type("chat") \
            .container_id(self._chat_id) \
            .page_size(10) \
            .sort_type("ByCreateTimeDesc") \
            .build()

        resp: ListMessageResponse = self._client.im.v1.message.list(req)
        if not resp.success():
            logger.warning("list_message failed: code=%s msg=%s", resp.code, resp.msg)
            return None

        items = resp.data.items or []
        for item in items:
            create_time = getattr(item, "create_time", "0")
            if int(create_time) <= int(since_ts):
                continue

            sender = getattr(item, "sender", None)
            if sender is None:
                continue
            sender_type = getattr(sender, "sender_type", "")
            if sender_type == "app":
                continue

            msg_type = getattr(item, "msg_type", "")
            if msg_type != "text":
                continue

            body = getattr(item, "body", None)
            if body is None:
                continue
            content_str = getattr(body, "content", "{}")
            try:
                content = json.loads(content_str)
                return content.get("text", "")
            except (json.JSONDecodeError, TypeError):
                return content_str

        return None
