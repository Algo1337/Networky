import discord

from discord import Embed
from ...utils.discord.messages import *


async def ver(message: discord.message):
    
    embed = Embed(title="Click Here For Latest Update!", description="Bot Information", color=discord.Color.green())
    embed.add_field(name="Bot Version", value="v1.0", inline=False)
    embed.add_field(name="Coded In", value="Python", inline=False)
    embed.add_field(name="Coded By", value="Networky Dev Team", inline=False)
    embed.add_field(name="Need Help?", value="Use The Help Command For Help (+help)", inline=False)
    embed.url = "https://youtube.com/"
    embed.set_image(url="https://cdn.discordapp.com/icons/1257679994944229528/6a6bf8a8a865255e3b36d752c01c7600.webp?size=160")
    embed.set_footer(text="Thanks For Using The Networky Moderation Bot.")


    await message.channel.send(embed=embed)