"""Lark Feedback MCP — control Cursor from your phone via Lark/Feishu."""

import os
import json
from typing import Dict, Optional

os.environ.setdefault("FASTMCP_LOG_LEVEL", "ERROR")

from fastmcp import FastMCP
from pydantic import Field

from lark_client import LarkClient

mcp = FastMCP("Lark Feedback MCP")

_client: Optional[LarkClient] = None


def _get_client() -> LarkClient:
    """Lazily initialise the LarkClient from config.json."""
    global _client
    if _client is not None:
        return _client

    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    _client = LarkClient(
        app_id=cfg["app_id"],
        app_secret=cfg["app_secret"],
        chat_id=cfg["chat_id"],
    )
    return _client


@mcp.tool()
def send_to_lark(
    message: str = Field(description="The message text to send to the Lark chat"),
) -> Dict[str, str]:
    """Send a message to the user's phone via Lark/Feishu.

    Use this to report progress, results, or ask the user a question.
    The user will see the message in the Lark app on their phone.
    """
    client = _get_client()
    ok = client.send_message(message)
    if ok:
        return {"status": "sent", "message": message}
    return {"status": "error", "message": "Failed to send message to Lark"}


@mcp.tool()
def wait_for_lark_input(
    prompt: str = Field(description="The prompt/question to send to the user before waiting"),
    predefined_options: list = Field(
        default=None,
        description="Optional predefined options shown to the user (list of strings)",
    ),
    timeout: int = Field(
        default=600,
        description="Max seconds to wait for a reply (default 600 = 10 min)",
    ),
) -> Dict[str, str]:
    """Send a prompt to the user's phone via Lark and wait for their reply.

    This blocks until the user replies in the Lark chat or timeout is reached.
    Use predefined_options to show quick-select choices (they are listed in the message).
    Returns the user's reply text.
    """
    client = _get_client()

    full_prompt = prompt
    if predefined_options:
        options_text = "\n".join(
            f"  {i+1}. {opt}" for i, opt in enumerate(predefined_options)
        )
        full_prompt = f"{prompt}\n\n可选项：\n{options_text}\n\n（直接回复数字或文字均可）"

    ok = client.send_message(full_prompt)
    if not ok:
        return {"interactive_feedback": "", "error": "Failed to send prompt to Lark"}

    reply = client.poll_user_message(timeout=timeout)
    if reply is None:
        return {"interactive_feedback": "", "error": "Timeout waiting for user reply"}

    if predefined_options and reply.strip().isdigit():
        idx = int(reply.strip()) - 1
        if 0 <= idx < len(predefined_options):
            reply = predefined_options[idx]

    return {"interactive_feedback": reply}


if __name__ == "__main__":
    mcp.run(transport="stdio")
