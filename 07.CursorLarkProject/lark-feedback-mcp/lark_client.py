"""Lark/Feishu API client for sending and receiving messages."""

import json
import time
import logging
from typing import Optional

import lark_oapi as lark
from lark_oapi.api.im.v1 import (
    CreateMessageRequest,
    CreateMessageRequestBody,
    CreateMessageResponse,
    ListMessageRequest,
    ListMessageResponse,
)

logger = logging.getLogger(__name__)


class LarkClient:
    """Wraps Lark SDK to provide simple send/receive message operations."""

    def __init__(self, app_id: str, app_secret: str, chat_id: str):
        self._chat_id = chat_id
        self._client = lark.Client.builder() \
            .app_id(app_id) \
            .app_secret(app_secret) \
            .log_level(lark.LogLevel.WARNING) \
            .build()
        self._last_seen_msg_id: Optional[str] = None

    def send_message(self, text: str) -> bool:
        """Send a text message to the configured chat. Returns True on success."""
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

        msg_id = resp.data.message_id
        self._last_seen_msg_id = msg_id
        return True

    def poll_user_message(
        self,
        timeout: int = 600,
        interval: float = 3.0,
    ) -> Optional[str]:
        """Poll the chat for new user (non-bot) messages.

        Blocks up to *timeout* seconds, checking every *interval* seconds.
        Returns the text content of the first new user message, or None on timeout.
        """
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
