"""
        [ Networky Discord Bot ]

        @title: Networky
        @author: Algorithm, Greek
        @since: 7/2/2024
"""
import os, discord, jishaku
from discord.ext import commands

from src.discord_utils.messages import Message

## Temporary Config Settings
class Config:
    prefix = "+"

    @staticmethod
    def get_all_commands() -> list:
        cmds = []
        files = os.listdir("src/commands/") # im blind... rerun
        if len(files) == 0:
            return cmds
    
        for file in files:
            if file.endswith(".py"):
                cmds.append(file.replace(".py", ""))

        return cmds #im bk


class Networky(commands.Bot):
    """ im thinking of doing it another way, for commands lol. i cant decide which is holding me up ol"""
    async def on_ready(self):
        await self.load_extension('jishaku')#fixed rerun.

        print(f"Firing up Networky Discord Bot....!", "Loading commands....!")
        self.commands = Config.get_all_commands()

        print("Commands loaded....!", f"Logged on as {self.user}....!")

    async def on_message(self, message):
        if message.author == self.user:
            return
            
        msg_data = Message(message)
        if msg_data.data.startswith(Config.prefix):
            for command in self.commands:
                if msg_data.data.startswith(f"{Config.prefix}{command}"):
                    print(f"[{message.author.name}] executed command -> {command}")
                    break

        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True






















client = Networky(intents=intents, command_prefix={Config.prefix})




client.run('MTI0Njk3ODcxMjI5ODE5MjkzNw.Gtdx1q.ntbXI4KoR2CcHDtFZTXCOyGuALke3rwoGUIdvU')