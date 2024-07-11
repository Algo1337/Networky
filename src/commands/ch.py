import discord
from discord import Embed
from ..tools.check_host import *
from ..discord_utils.messages import *

async def ch(message: discord.Message):
    msg = Message(message)

    if len(msg.args) < 2:
        embed = Embed(title="[ X ] Error, Invalid arguments", color=discord.Color.red())
        embed.add_field(name="Usage", value="+ch <ip>")
        await message.channel.send(embed=embed)
        return 
    
    api = CheckHostSDK(25)
    search = api.TCPPing(msg.args[1])

    if search is None or search is False:
        embed = Embed(title="Error", description="An error occurred while checking the host.", color=discord.Color.red())
        await message.channel.send(embed=embed)
        return 
    
    embed = Embed(title="TCP Ping Result", description=search, color=discord.Color.green())
    await message.channel.send(embed=embed)