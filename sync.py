import os
from notion_client import Client

notion = Client(auth=os.environ["NOTION_TOKEN"])

PAGE_ID = os.environ["NOTION_PAGE_ID"]

def get_blocks(block_id):
    blocks = []
    cursor = None

    while True:
        response = notion.blocks.children.list(
            block_id=block_id,
            start_cursor=cursor
        )

        blocks.extend(response["results"])

        if not response["has_more"]:
            break

        cursor = response["next_cursor"]

    return blocks


def rich_text(block):
    if "rich_text" not in block:
        return ""

    return "".join(
        t["plain_text"]
        for t in block["rich_text"]
    )


blocks = get_blocks(PAGE_ID)

md = []

for block in blocks:

    t = block["type"]

    if t == "heading_1":
        md.append("# " + rich_text(block[t]))

    elif t == "heading_2":
        md.append("## " + rich_text(block[t]))

    elif t == "heading_3":
        md.append("### " + rich_text(block[t]))

    elif t == "paragraph":
        md.append(rich_text(block[t]))

    elif t == "bulleted_list_item":
        md.append("- " + rich_text(block[t]))

    elif t == "numbered_list_item":
        md.append("1. " + rich_text(block[t]))

    elif t == "code":
        md.append("```")
        md.append(rich_text(block[t]))
        md.append("```")

with open("README.md", "w", encoding="utf-8") as f:
    f.write("\n\n".join(md))