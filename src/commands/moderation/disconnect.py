import discord

async def disconnect(message: discord.message) -> bool:
    if not message.author.voice:
        return
    
    voice_client = message.guild.voice_client
    if not voice_client:
        return
    
    await voice_client.disconnect()
    await message.channel.send("Left the VC!")