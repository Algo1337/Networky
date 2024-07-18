import discord

from discord import Embed
from ...discord_utils.messages import *


async def ver(message: discord.message):
    
    embed = Embed(title="Bot Info", description="List Of Bot Information", color=discord.Color.green())
    embed.add_field(name="Bot Version", value="v1.0", inline=True)
    embed.add_field(name="Coded In", value="Python", inline=True)
    embed.add_field(name="Coded By", value="Networky Dev Team", inline=True)
    embed.add_field(name="Need Help?", value="Use The Help Command For Help (+help)", inline=False)
    embed.set_image(url="https://shorturl.at/CLtQb")
    embed.set_footer(text="Thanks For Using The Networky Moderation Bot.")


    await message.channel.send(embed=embed)