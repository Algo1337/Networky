import discord, time

from ...utils.discord.messages import *

async def purge(message: discord.message) -> bool:
    msg = Message(message)

    if not message.author.guild_permissions.administrator:
        await message.channel.send("You're not an admin sir!")
        
    if len(msg.args) < 2:
        await message.channel.send("Error")

    await message.delete()

    if isinstance(msg.args[1], int):
        await message.channel.purge(limit=int(msg.args[1]))

    if isinstance(msg.args[1], str):
        async for msgg in message.channel.history(limit=int(msg.args[2])):  # Fetch the last 100 messages
            if f"{msgg.author.id}" == msg.args[1].replace("<", "").replace(">", "").replace("@", ""):
                time.sleep(.45)
                await msgg.delete()

    return True