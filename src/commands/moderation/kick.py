import discord 

from ...utils.discord.messages import *

async def kick(message: discord.message) -> bool:
    msg = Message(message)
    
    if not message.author.guild_permissions.administrator:
        await message.channel.send("You're not an admin sir!")
        return
    
    for member in message.guild.members:
        if f"{member.id}" == f"{msg.args[1]}":
            await message.channel.send(f"User Kicked <@{msg.args[1]}>")
            return await member.kick()
        
    await message.channel.send("[ X ]  Unable to find user....!")

    return True