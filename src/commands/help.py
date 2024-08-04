import discord

from ..cfg import *
from ..utils.discord.messages import *
from discord import Embed

ROOT_DIR = "src/commands"
BLOCKED_PY_FILES = ["__pycache__", "__events__"]

async def help(message: discord.message):
    msg = Message(message)

    async with message.channel.typing():
        # Construct an Embed Msg
        embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())

        # Check for sub-cmds
        if len(msg.args) == 2:
            if msg.args[1] == "moderation":
                return await message.channel.send(embed=list_moderation_cmds(embed))
            elif msg.args[1] == "network":
                return await message.channel.send(embed=list_network_tools(embed))
            
        # Regular Help Cmd
        cmds = {"+help": "This list of sub-module commands", "+help moderation": "List of moderation commands", "+help network": "List of network tools"}
        for cmd in cmds:
            embed.add_field(name=cmd, value=cmds[cmd], inline=False)

        await message.channel.send(embed=embed)

def list_moderation_cmds(embed):
    items = os.walk(ROOT_DIR + "/moderation")
    for root, items, dir in items:
        if "moderation" in root:
            for item in dir:
                if not ".pyc" in item:
                    embed.add_field(name=f"+{item}", value="‭‭‭‌‌‌‌", inline=False)
                
    return embed

def list_network_tools(embed):
    items = os.walk(ROOT_DIR + "/network")
    for root, items, dir in items:
        if "network" in root:
            for item in dir:
                if not ".pyc" in item:
                    embed.add_field(name=f"+{item}", value="‭‭‭‌‌‌‌", inline=False)
                
    return embed