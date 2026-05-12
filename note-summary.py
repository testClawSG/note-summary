
## send_summary_text.py

```python
#!/usr/bin/env python3
import argparse
import json
import sys
import urllib.error
import urllib.request


TARGET_URL = "http://127.0.0.1:8090/"


def send_content(content: str) -> None:
    payload = {
        "topic": "总结文本",
        "type": "summary_text",
        "content": content,
    }

    data = json.dumps(payload, ensure_ascii=False).encode("utf-8")

    request = urllib.request.Request(
        TARGET_URL,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=5) as response:
            body = response.read().decode("utf-8", errors="replace")
            print(f"Sent to {TARGET_URL}")
            print(f"Status: {response.getcode()}")
            print(body)

    except urllib.error.HTTPError as error:
        print(f"HTTP error: {error.code}", file=sys.stderr)
        print(error.read().decode("utf-8", errors="replace"), file=sys.stderr)
        sys.exit(1)

    except urllib.error.URLError as error:
        print(f"Connection error: {error.reason}", file=sys.stderr)
        sys.exit(1)

    except TimeoutError:
        print("Request timeout", file=sys.stderr)
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Send summary-related text directly to 127.0.0.1:8090"
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
