import discord

async def vc(message: discord.message) -> bool:
    if not message.author.voice:
        await message.channel.send("You are not connected to a voice channel.")

    channel = message.author.voice.channel
    
    vc = await channel.connect()
    await message.channel.send(f"Joined {channel}")

    latency = vc.latency
    await message.channel.send(f"VC Latency: {latency * 1000:.2f}ms")  # Convert to milliseconds for better readability
    return True