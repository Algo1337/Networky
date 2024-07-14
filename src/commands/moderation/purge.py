import discord

from ...discord_utils.messages import *

async def purge(message: discord.message) -> bool:
    msg = Message(message)

    await message.channel.purge(limit=1000)