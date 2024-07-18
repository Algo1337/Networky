import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.guild_messages = True
intents.guilds = True

async def unlock(message, channel: discord.TextChannel = None, *, reason="No reason provided."):
    channel = channel or message.channel

    # Update channel permissions to allow sending messages
    overwrite = channel.overwrites_for(message.guild.default_role)
    overwrite.send_messages = True
    await channel.set_permissions(message.guild.default_role, overwrite=overwrite, reason=f"Unlocked by {message.author} for {reason}")

    await message.send(f"🔓 {channel.mention} has been unlocked by {message.author.mention} for {reason}")