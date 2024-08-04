import os

BLOCKED_PY_FILES = ["__pycache__", "__events__"]

"""
    GET ALL FILES
"""
def get_cmds_files(root_dir):
    items = os.walk(root_dir)
    for root, items, dir in items:
        if "moderation" in root:
            for item in dir:
                print(f"File: {root.replace('\\', '/').replace(root_dir, "")[1:]}/{item}")


def get_all_sub_cmds(root_dir):
    items = os.walk(root_dir)
    for root, items, dir in items:
        if "moderation" in root:
            print(f"File: {root.replace('\\', '/').replace(root_dir, "")[1:]}")

get_cmds_files("src/commands")