"""
        [ Networky Discord Bot ]

        @title: Networky
        @author: Algorithm, Greek
        @since: 7/2/2024
"""
import os, discord

from src.cogs import *
from src.discord_utils.messages import Message

## Temporary Config Settings
class Config:
    prefix = "+"

    @staticmethod
    def load_all_cogs() -> None:
        cmds = {}
        files = os.listdir("src/commands/")
        if len(files) == 0:
            return cmds

        for file in files:
            if file.endswith(".py"):
                cmds[file.replace(".py", "")] = Library(f"src.commands.{file.replace(".py", "")}")

        return cmds

class Networky(discord.Client):
    async def on_ready(self):
        print(f"Firing up Networky Discord Bot....!", "Loading commands....!")
        self.commands = Config.load_all_cogs()

        print("Commands loaded....!", f"Logged on as {self.user}....!")

    async def on_message(self, message):
        if message.author == self.user:
            return
            
        msg_data = Message(message)
        if msg_data.data.startswith(Config.prefix):
            for command in self.commands:
                if msg_data.data.startswith(f"{Config.prefix}{command}"):
                    print(f"[{message.author.name}] executed command -> {command}")
                    cmd_test = await self.commands[command].execute_method(command, message)
                    if not cmd_test:
                        await message.channel.send("Failed to find command or corrupted Lib()")
                    break

        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True






















client = Networky(intents=intents, command_prefix={Config.prefix})




client.run('MTI0Njk3ODcxMjI5ODE5MjkzNw.Gtdx1q.ntbXI4KoR2CcHDtFZTXCOyGuALke3rwoGUIdvU')