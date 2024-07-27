import discord

from ..cfg import *
from discord import Embed


__EVENTS_METHODS__ = ["__events__", "on_msg_event.py", "on_vc_event.py"]
async def help(message: discord.message):
    walk = os.walk("src/commands/")

    # Construct an Embed Msg
    embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())
    
    for root,dirs,files in walk:
        if "__pycache__" in root: continue # ignore __pycache__ and 
        for cmd in files:
            if cmd.startswith("."): continue # ignore dot files
            if cmd in __EVENTS_METHODS__: continue # ignore this specific file
            cmd = cmd.replace(".py", "")
            embed.add_field(name=cmd, value=f'{Config.prefix}{cmd}', inline=False)

    await message.channel.send(embed=embed)