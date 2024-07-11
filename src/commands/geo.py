import discord
import requests
from discord import Embed
from ..discord_utils.messages import *

async def geo(message: discord.Message):
    msg = Message(message)

    if len(msg.args) < 2:
        embed = Embed(title="[ X ] Error, Invalid arguments", color=discord.Color.red())
        embed.add_field(name="Usage", value="+geo <ip>")
        await message.channel.send(embed=embed)
        return 
    
    resp = requests.get(f"https://ipwho.is/{msg.args[1]}")
    
    if resp.status_code != 200:
        embed = Embed(title="Error", description="An error occurred while fetching geo information.", color=discord.Color.red())
        await message.channel.send(embed=embed)
        return 
    
    embed = Embed(title="Geolocation Information", description=resp.text, color=discord.Color.blue())
    await message.channel.send(embed=embed)
