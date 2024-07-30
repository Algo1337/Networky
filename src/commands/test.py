import discord

from ..cogs import *
from ..utils.discord.messages import *

async def test(message: discord.message, lib: DiscordCogs):

    chk = await is_author_dev(message.author.roles)
    if f"{message.author.id}" != "1235776145819959318" and not chk:
        return await message.channel.send("[ X ] Error, You cannot use...!")
    
    if f"{message.guild.id}" == "1244277388351635457":
        return await message.channel.reply("[ X ] Error, Wrong server to use this command")

    msg = Message(message)
    data = msg.data.replace(msg.args[0], "").replace(msg.args[1].split("\n")[0], "").replace("`", "")
    
    if not "```" in msg.data:
        await message.reply("[ X ] Error, Missing code snippet....!")
    
    add_new_cmd(lib, msg.args[1].split('\n')[0], data)

    await message.reply("Save and updated")

async def is_author_dev(roles: list[str]) -> bool:
    for role in roles:
        if f"{role.name}" == "Networky Dev":
            return True
        
    return False

def add_new_cmd(libs: DiscordCogs, cmd_file: str, code: str):
    new_cmd = open(f"src/commands/{cmd_file}", "w+")
    new_cmd.write(code)
    new_cmd.close()

    gg = Library(f"src.commands.{cmd_file.replace('.py', '')}");
    libs.commands[cmd_file.replace(".py", "")] = gg;