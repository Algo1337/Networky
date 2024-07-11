import discord
import requests
from discord import Embed
from datetime import datetime
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
    
    data = resp.json()
    
    embed = Embed(title="Geolocation Information", color=discord.Color.blue())
    embed.add_field(name="IP", value=data["ip"], inline=True)
    embed.add_field(name="Hostname", value=data["hostname"], inline=True)
    embed.add_field(name="City", value=data["city"], inline=True)
    embed.add_field(name="Region", value=data["region"], inline=True)
    embed.add_field(name="Country", value=data["country"], inline=True)
    embed.add_field(name="ISP", value=data["isp"], inline=True)
    
    image_url = "https://www.freepnglogos.com/uploads/globe-png/globe-telecom-septier-15.png"
    embed.set_image(url=image_url)
    
    copyright_url = "https://www.citypng.com/public/uploads/preview/hd-copyright-all-rights-reserved-red-stamp-png-11662464508s8pru5hcxm.png"
    embed.set_footer(text="Networky 2024 ©", icon_url=copyright_url)
    
    embed.timestamp = datetime.utcnow()
    
    await message.channel.send(embed=embed)

    await message.channel.send(embed=embed)