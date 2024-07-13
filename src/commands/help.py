import discord

from ..cfg import *
from discord import Embed

async def help(message: discord.message):
    files = os.listdir("src/commands/")
    # Construct an Embed Msg
    embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())
    for cmd in files:
        if not os.path.isdir(cmd):
            embed.add_field(name=cmd, value=f"{Config.prefix}{cmd}", inline=False)
        else: continue

    await message.channel.send(embed=embed)