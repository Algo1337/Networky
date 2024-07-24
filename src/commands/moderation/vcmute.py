import discord

from ...utils.discord.messages import *

async def vcmute(message: discord.message):
    msg = Message(message)

    if len(msg.args) < 2:
        return await message.channel.send("Error")
    
    if not message.author.guild_permissions.administrator:
        return await message.channel.send("You do not have permission to manage roles.")
    
    if not message.author.voice:
        return await message.channel.send("You are not connected to a voice channel.")
    
    voice_channel = message.author.voice.channel
    
    for member in voice_channel.members:
        if f"{member.id}" == f"{msg.args[1]}":
            await member.edit(mute=True)
            return await message.channel.send(f"{member.display_name} has been server muted.")
        
    return await message.channel.send("User not in VC")