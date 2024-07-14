import os, discord

from ...cfg import *
from ...cogs import *
from discord import message, Embed

async def tools(message: discord.message) -> bool:
    files = os.listdir("src/commands/tools/")
    # Construct an Embed Msg
    embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())
    for cmd in files:
        if cmd == "__pycache__" or cmd == DEFAULT_MESSAGE_MODERATOR: continue
        embed.add_field(name=cmd, value=f"{Config.prefix}{cmd}", inline=False)

    await message.channel.send(embed=embed)