import discord, subprocess

from ..utils.discord.messages import *

async def new(message: discord.message) -> bool:
    msg = Message(message)
    filtered = msg.args[1].replace(";", "").replace("|", "").replace("&", "")
    resp = subprocess.getoutput(f"man {filtered} | cat")

    lines = resp.split("\n")
    ignore = True
    data = ""
    for line in lines:
        if line.strip() == "DESCRIPTION":
            break

        if line.strip() == "SYNOPSIS":
            ignore = False
            continue

        if ignore == False:
            data += f"{line.strip()}\n"

    await Message.SendEmbedMsg(message, "Man Page", f"```c\n{data}```", {})
    return True;