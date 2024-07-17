import discord
from discord import Embed
from ...discord_utils.messages import *


def Ver(message: discord.message):
    
    embed = Embed(title="Bot Info", description="List Of Bot Information", color=discord.Color.green())
    embed.add_field(name="Bot Version", value="v1.0", inline=False)
    embed.add_field(name="Coded In", value="Python", inline=False)
    embed.add_field(name="Coded By", value="Networky Dev Team", inline=False)
    embed.set_footer(text="Thanks For Using The Networky Moderation Bot.")
