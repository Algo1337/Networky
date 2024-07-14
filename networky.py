"""
        [ Networky Discord Bot ]

        @title: Networky
        @author: Algorithm, Greek
        @since: 7/2/2024
"""
import discord

from src.cfg import *
from src.cogs import *

from src.discord_utils.messages import Message

class Networky(discord.Client, DiscordCogs):
    async def on_ready(self):
        print(f"[ + ] Firing up Networky Discord Bot....!\n[ + ] Loading commands....!")
        print(f"[ + ] Commands loaded....!\n[ + ] Logged on as {self.user}....!")

    async def on_message(self, message):
        if message.author == self.user:
            return
            
        msg_data = Message(message)
        if "message_watch" in self.commands:
            await self.ExecuteCmd("message_watch", message)

        if not msg_data.data.startswith(Config.prefix):
            return
        
        if not await self.ExecuteCmd(msg_data.args[0].replace(Config.prefix, ""), message):
            return await message.channel.send("Failed to find command or corrupted Lib()")

        print(f'[ + ] Message from {message.author}: {message.content}')


c = DiscordCogs("src/commands/")
intents = discord.Intents.default()
intents.message_content = True
client = Networky(intents=intents, command_prefix={Config.prefix})



























client.run('MTI0Njk3ODcxMjI5ODE5MjkzNw.Gtdx1q.ntbXI4KoR2CcHDtFZTXCOyGuALke3rwoGUIdvU')