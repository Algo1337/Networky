import discord
from discord import Embed

# from ...tools.check_host import *

from src.tools.check_host import *
from ...utils.discord.messages import *

"""
    Check-Host Pinging API
"""
async def ping(message: discord.Message):
    msg = Message(message)
    if len(msg.args) < 3:
        embed = Embed(title="[ X ] Error, Invalid arguments", color=discord.Color.red())
        embed.add_field(name="Usage", value="+ping <ip> <nodes>")
        await message.channel.send(embed=embed)
        return 
    
    # Send a wait msg and process the data
    wait_msg = await message.channel.send("Pinging IP, Please wait.....")

    api = CheckHostSDK(msg.args[2])
    search = api.TCPPing(msg.args[1])

    # Retrieve and delete the wait message
    msg_todel = await message.channel.fetch_message(int(wait_msg.id))
    await msg_todel.delete()

    # Check for validate Check-Host results
    if search is None or search is False:
        embed = Embed(title="Error", description="An error occurred while checking the host.", color=discord.Color.red())
        await message.channel.send(embed=embed)
        return 
    
    # Construct an Embed Msg
    embed = Embed(title="TCP Ping Result", description="List of Check-Host Results", color=discord.Color.green())
    for k in search:
        embed.add_field(name=f"{search[k].COUNTRY_NAME}, {search[k].COUNTRY_STATE} | {k}", value=f"IP: {search[k].IP_ADDRESS} | MS Response: {search[k].RESPONSE_TIME}", inline=False)

    await message.channel.send(embed=embed)