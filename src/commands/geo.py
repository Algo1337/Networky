import discord, requests

from ..discord_utils.messages import *

async def geo(message: discord.message):
    msg = Message(message)

    if len(msg.args) < 2:
        await message.channel.send("[ X ] Error, Invalid arguments\nUsage: +geo <ip>")
        return 
    
    resp = requests.get(f"https://ipwho.is/{msg.args[1]}")
    await message.channel.send(resp.text)