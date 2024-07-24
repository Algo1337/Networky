import discord, subprocess, validators

from ...discord_utils.messages import *

async def nmap(message: discord.message) -> bool:
    msg = Message(message)

    if len(msg.args) < 2:
        return await message.channel.send("[ X ] Error, Invalid arguments\nUsage: +nmap <ip>")
    
    if not validators.ipv4(msg.args[1]):
        return await message.channel.send("Error KEEED")
    
    wait_msg = await message.channel.send("Nmaping, Please wait....")
    resp = subprocess.getoutput(f"nmap {msg.args[1]}")
    await wait_msg.delete()
    await message.channel.send(f"```{resp}```")
    return True