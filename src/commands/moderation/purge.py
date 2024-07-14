import discord

from ...discord_utils.messages import *

async def purge(message: discord.message) -> bool:
    msg = Message(message)

    if len(msg.args) < 2:
        await message.channel.send("Error")

    if isinstance(int(msg.args[1]), int):
        await message.channel.purge(limit=int(msg.args[1]))