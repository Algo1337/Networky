import discord

from ..tools.check_host import *
from ..discord_utils.messages import *

async def ch(message: discord.message):
    msg = Message(message)

    if len(msg.args) < 2:
        await message.channel.send("[ X ] Error, Invalid arguments\nUsage: +ch <ip>")
        return 
    
    api = CheckHostSDK(25)
    search = api.TCPPing(msg.args[1])

    if search == None or search == False:
        await message.channel.send("ERROR")
        return 
    
    await message.channel.send(search)