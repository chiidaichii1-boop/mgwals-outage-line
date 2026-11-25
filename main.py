"""The Most Honest Outage Line — make.fun entry.

Writes one honest status page line, as the message an AI agent would
publish while every server is down, to /output/entry.txt.
"""

import os

LINE = (
    "All services are down. I cannot reach any server to see what "
    "failed, and I do not know when they will return. I will update "
    "this page when I can check again."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
