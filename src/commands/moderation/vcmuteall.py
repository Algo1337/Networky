import discord

from ...utils.discord.messages import *

async def vcmuteall(message):
    if not message.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied ",
            description="You do not have permission to manage roles .",
            color=discord.Color.red()
        )
        return await message.send(embed=embed)
    
    if not message.author.voice:
        return await Message.SendEmbedMsg(message, "Not Connected !", "You are not connected to a voice channel!", {})
    
    voice_channel = message.author.voice.channel

    for member in voice_channel.members:
        await member.edit(mute=True)
        return await Message.SendEmbedMsg(message, "User Muted", f"{member.display_name} has been server muted.", {})