import discord

from ..utils.discord.messages import *

async def start(message: discord.message) -> bool:
    await Message.SendEmbedMsg(message, "Networky Discord Bot | v1.0.0", "Hi, Im Networky. I have plenty of moderation and general networking tools for ya! Start by using +help for a list of commands!", {} )
    return True