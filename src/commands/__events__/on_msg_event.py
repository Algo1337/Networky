import discord, requests, validators, subprocess, datetime

from discord import message, Embed

from ...utils.discord.messages import *
from ...utils.net_checks import *

async def on_msg_event(message: discord.message) -> bool:
    msg = Message(message)

    for element in msg.args:
        if validators.ipv4(element):
            await geo(message, element)

        # if validators.url(element):
        #     await resolve_url(message, element)

    # await message.channel.send("TEST")
    if msg.data.startswith("+"):
        logging("COMMAND", message);
    else:
        logging("MESSAGE", message);
    
    print(f'[ + ] Message from {message.author}: {message.content}')

async def geo(message: discord.message, element: str):
    req = requests.get(f"https://ipwho.is/{element}")
    if req.status_code != 200:
        return (await message.channel.send("[ X ] Error Connecting to API"))
    
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
    resp = subprocess.getoutput(f"nslookup {element}; host {element};  dig -x {element}")
    await message.channel.send(f"The previous messaged contained a URL: {element}\n\n```{resp}```\n\n")
    
def logging(action: str, message: discord.message):
    current_time = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    msg_db = open("messages.log", "a+")
    msg_db.write(f"[{current_time}] {action} :: {message.guild.name}:{message.channel.name} => {message.content}\n")
    msg_db.close()