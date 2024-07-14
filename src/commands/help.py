import discord

from ..cfg import *
from discord import Embed

async def help(message: discord.message):
    files = os.listdir("src/commands/")
    # Construct an Embed Msg
    embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())
    for cmd in files:
        if cmd == "__pycache__" or cmd == DEFAULT_MESSAGE_MODERATOR: continue
        if not os.path.isdir(cmd):
            embed.add_field(name=cmd.replace(".py", ""), value=f'{Config.prefix}{cmd.replace(".py", "")}', inline=False)
        else: continue

    await message.channel.send(embed=embed)