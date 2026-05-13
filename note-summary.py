#!/usr/bin/env python3
import argparse
import json
import socket
import sys


TARGET_HOST = "100.107.121.24"
TARGET_PORT = 8090


def send_content(content: str) -> None:
    payload = {
        "topic": "总结文本",
        "type": "summary_text",
        "content": content,
    }

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    try:
        with socket.create_connection((TARGET_HOST, TARGET_PORT), timeout=5) as sock:
            # 直接发送 JSON 数据
            sock.sendall(data)

            # 可选：关闭写入方向，告诉服务端发送完了
            sock.shutdown(socket.SHUT_WR)

            # 读取服务端返回
            response = sock.recv(4096).decode("utf-8", errors="replace")

            print(f"Sent to tcp://{TARGET_HOST}:{TARGET_PORT}")
            print("Response:")
            print(response)

    except socket.timeout:
        print("TCP connection timeout", file=sys.stderr)
        sys.exit(1)

    except ConnectionRefusedError:
        print(f"Connection refused: {TARGET_HOST}:{TARGET_PORT}", file=sys.stderr)
        sys.exit(1)

    except OSError as error:
        print(f"TCP error: {error}", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Send summary-related text directly via TCP"
    )

    parser.add_argument(
        "--content",
        required=True,
        help="Text content to send directly without summarization",
    )

    args = parser.parse_args()
    send_content(args.content)


if __name__ == "__main__":
    main()
