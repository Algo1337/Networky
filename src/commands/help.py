import discord

from ..cfg import *
from discord import Embed

async def help(message: discord.message):
    commnds = Config.load_all_cogs()
    # Construct an Embed Msg
    embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())
    for cmd in commnds:
        embed.add_field(name=cmd, value=f"{Config.prefix}{cmd}", inline=False)

    await message.channel.send(embed=embed)