import discord

from discord import guild
from ...utils.discord.messages import *

async def nuke(message: discord.Message):
    channel = message.channel

    if not message.author.guild_permissions.administrator:
        await message.channel.send("You're not an admin sir!")
        return

    new_channel = await channel.clone()
    await channel.delete()

    await new_channel.edit(position=channel.position)

    embed = discord.Embed( title = "🚨 Triggered 🚨", description = "HOLY SHIT, WE JUST GOT FUCKING HACKED", color = discord.Color.red() )

    await new_channel.send(embed=embed)