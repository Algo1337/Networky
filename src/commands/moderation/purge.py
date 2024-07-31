import discord

from ...utils.discord.messages import *

async def purge(message: discord.message) -> bool:
    msg = Message(message)

    if not message.author.guild_permissions.administrator:
        await message.channel.send("You're not an admin sir!")
        
    if len(msg.args) < 2:
        await message.channel.send("Error")

    if isinstance(int(msg.args[1]), int):
        await message.channel.purge(limit=int(msg.args[1]))

    return True