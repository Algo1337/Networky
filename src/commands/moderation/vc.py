import discord, asyncio

async def vc(message: discord.message) -> bool:
    if not message.author.voice:
        await message.channel.send("You are not connected to a voice channel.")

    channel = message.author.voice.channel
    
    vc = await channel.connect()

    start_time = asyncio.get_event_loop().time()
    await asyncio.sleep(1)
    end_time = asyncio.get_event_loop().time()

    latency = (end_time - start_time) * 1000
    await message.channel.send(f"Joined VC | Latency: {latency}ms")  # Convert to milliseconds for better readability
    return True