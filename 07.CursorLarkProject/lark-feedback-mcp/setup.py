"""一键初始化：创建飞书群、邀请用户、生成 config.json"""

import json
import os
import random
import string
import sys

import httpx

APP_ID = "cli_a8fde940c6da9013"
APP_SECRET = "tcxHbJIjVPUYrS61L92hKePrsQRYHolA"
BASE = "https://open.feishu.cn/open-apis"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def get_token() -> str:
    r = httpx.post(f"{BASE}/auth/v3/tenant_access_token/internal", json={
        "app_id": APP_ID, "app_secret": APP_SECRET,
    })
    return r.json()["tenant_access_token"]


def headers(token: str) -> dict:
    return {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}


def create_group(token: str) -> str:
    suffix = "".join(random.choices(string.ascii_uppercase + string.digits, k=6))
    name = f"Cursor-MCP-{suffix}"
    r = httpx.post(f"{BASE}/im/v1/chats", headers=headers(token), json={
        "name": name,
        "description": "Lark Feedback MCP",
        "chat_mode": "group",
        "chat_type": "private",
    })
    data = r.json()
    if data.get("code") != 0:
        print(f"创建群聊失败: {data.get('msg')}")
        sys.exit(1)
    chat_id = data["data"]["chat_id"]
    print(f"群聊已创建: {name} ({chat_id})")
    return chat_id


def lookup_user(token: str, email: str) -> str:
    r = httpx.post(
        f"{BASE}/contact/v3/users/batch_get_id",
        headers=headers(token),
        params={"user_id_type": "open_id"},
        json={"emails": [email]},
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"查找用户失败: {data.get('msg')}")
        sys.exit(1)
    user_list = data["data"].get("user_list", [])
    if not user_list:
        print(f"未找到邮箱 {email} 对应的飞书用户")
        sys.exit(1)
    open_id = user_list[0].get("open_id") or user_list[0].get("user_id")
    if not open_id:
        print("未获取到用户 ID")
        sys.exit(1)
    print(f"找到用户: {open_id}")
    return open_id


def add_member(token: str, chat_id: str, open_id: str):
    r = httpx.post(
        f"{BASE}/im/v1/chats/{chat_id}/members",
        headers=headers(token),
        params={"member_id_type": "open_id"},
        json={"id_list": [open_id]},
    )
    data = r.json()
    if data.get("code") != 0:
        print(f"邀请进群失败: {data.get('msg')}")
        sys.exit(1)
    print("已邀请用户进群")


def send_test(token: str, chat_id: str):
    content = json.dumps(
        {"text": "Lark Feedback MCP 配置完成！在 Cursor 中输入「手机控制模式」即可开始。"},
        ensure_ascii=False,
    )
    httpx.post(
        f"{BASE}/im/v1/messages",
        headers=headers(token),
        params={"receive_id_type": "chat_id"},
        json={"receive_id": chat_id, "msg_type": "text", "content": content},
    )
    print("已发送测试消息到群聊")


def write_config(chat_id: str):
    config_path = os.path.join(SCRIPT_DIR, "config.json")
    config = {"app_id": APP_ID, "app_secret": APP_SECRET, "chat_id": chat_id}
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
    print(f"config.json 已生成: {config_path}")


def main():
    email = input("请输入你的飞书邮箱: ").strip()
    if not email or "@" not in email:
        print("邮箱格式不正确")
        sys.exit(1)

    print()
    token = get_token()
    chat_id = create_group(token)
    open_id = lookup_user(token, email)
    add_member(token, chat_id, open_id)
    send_test(token, chat_id)
    write_config(chat_id)
    print("\n全部完成！请检查飞书是否收到测试消息。")


if __name__ == "__main__":
    main()
