import discord

from discord import guild
from ...utils.discord.messages import *

async def nuke(message: discord.message):
    channel = message.channel

    if not message.author.guild_permissions.administrator:
        await message.channel.send("You're not an admin sir!")
        
    new_channel = await channel.clone()
    await channel.delete()
    await new_channel.edit(position=channel.position)

    await new_channel.send(f"HOLY SHIT, WE JUST GOT FUCKING HACKED")