import discord

from ...utils.discord.messages import *
from discord.utils import get


async def joinss(message: discord.message) -> bool:
    msg = Message(message)
    if len(msg.args) != 2:
        await message.channel.send("Incorrect usage. Use: !joinss <user_id>")
        return
    
    if not isinstance(msg.args[1], int):
        return await message.channel.send("[ x ] Invalid argument. Usage: +joinss <user_id>")

    user_id = int(msg.args[1])
    
    user = await message.guild.fetch_member(user_id)
    if not user:
        return (await message.channel.send("[ x ] User not found!"))
    
    # Check if the user is currently in a voice channel and screen sharing
    if not user.voice or not user.voice.self_stream:
        await message.channel.send(f"{user.display_name} is not currently screen sharing in a voice channel.")
        return
    
    # Attempt to connect to the voice channel where the user is screen sharing
    try:
        voice_channel = user.voice.channel
        voice_client = await voice_channel.connect()
        await message.channel.send(f"Joined {user.display_name}'s screen share session in {voice_channel.name}.")
    except discord.ClientException:
        await message.channel.send(f"Failed to join {user.display_name}'s screen share session.")
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")