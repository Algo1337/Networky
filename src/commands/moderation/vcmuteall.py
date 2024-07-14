import discord

async def vcmuteall(message: discord.message):
    if not message.author.guild_permissions.administrator:
        return await message.channel.send("You do not have permission to manage roles.")
    
    if not message.author.voice:
        return await message.channel.send("You are not connected to a voice channel.")
    
    voice_channel = message.author.voice.channel

    for member in voice_channel.members:
        await member.edit(mute=True)
        await message.channel.send(f"{member.display_name} has been server muted.")