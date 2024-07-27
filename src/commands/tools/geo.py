import discord, requests
from discord import Embed

# from ...discord_utils.messages import *

from ...utils.discord.messages import *

async def geo(message: discord.message):
    msg = Message(message)

    if len(msg.args) < 2:
        await message.channel.send("[ X ] Error, Invalid arguments\nUsage: +geo <ip>")
        return 
    
    req = requests.get(f"https://ipwho.is/{msg.args[1]}")
    if req.status_code != 200:
        return (await message.channel.send("Err Connecting to API"))
    
    resp = req.json()

    # Construct an Embed Msg
    embed = Embed(title="Geo Location Result", description=f"Geo Location Of {msg.args[1]}", color=discord.Color.green())
    for k in resp:
        if "flag" in k or "timezone" == k: continue

        if "connection" == k:
            for nk in resp["connection"]:
                embed.add_field(name=nk.capitalize(), value=resp[k][nk], inline=True)

            continue

        embed.add_field(name=k.capitalize(), value=resp[k], inline=True)

    await message.channel.send(embed=embed)