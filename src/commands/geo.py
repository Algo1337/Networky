import discord
import Nominatim

async def geo(message: discord.message):
    nom = Nominatim(user_agent="discord-bot")
