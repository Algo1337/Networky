import discord, requests, validators, subprocess

from discord import message, Embed

from ..discord_utils.messages import *
from ..utils.net_checks import *

async def message_watch(message: discord.message) -> bool:
    msg = Message(message)

    for element in msg.args:
        if validate_ipv4_format(element):
            await geo(message, element)

        if validators.url(element):
            await resolve_url(message, element)

    # await message.channel.send("TEST")

async def geo(message: discord.message, element: str):
    msg = Message(message)
    req = requests.get(f"https://ipwho.is/{element}")
    if req.status_code != 200:
        return (await message.channel.send("Err Connecting to API"))
    
    resp = req.json()

    # Construct an Embed Msg
    embed = Embed(title="Geo Location Result", description=f"The previous messaged contained a IP: {element}\nGeo Location Of {element}", color=discord.Color.green())
    for k in resp:
        if "flag" in k or "timezone" == k: continue

        if "connection" == k:
            for nk in resp["connection"]:
                embed.add_field(name=nk.capitalize(), value=resp[k][nk], inline=True)

            continue

        embed.add_field(name=k.capitalize(), value=resp[k], inline=True)

    await message.channel.send(embed=embed)

async def resolve_url(message: discord.message, element: str):
    msg = Message(message)

    resp = subprocess.getoutput(f"nslookup {element}; host {element};  dig -x {element}")
    await message.channel.send(f"The previous messaged contained a URL: {element}\n\n```{resp}```")
    