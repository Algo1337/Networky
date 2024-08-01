"""
        [ Networky Discord Bot ]

        @title: Networky
        @author: Algorithm
        @since: 7/2/2024
"""
import discord, asyncio, threading

from src.cfg import *
from src.cogs import *

from src.utils.discord.messages import Message

class Networky(discord.Client, DiscordCogs):
    async def on_ready(self):
        if len(self.commands) == 0:
            print("[ x ] No commands were loaded....!")

        print(f"[ + ] Firing up Networky Discord Bot....!\n[ + ] Loading commands....!")
        print(f"[ + ] Commands loaded....!\n[ + ] Logged on as {self.user}....!")

    async def on_message(self, message):
        if message.author == self.user:
            return
            
        msg_data = Message(message)
        if "on_msg_event" in self.commands:
            await self.ExecuteMsgModerator("on_msg_event", message)

        if not msg_data.data.startswith(Config.prefix):
            return
        
        if msg_data.cmd == "+test":
            return await self.ExcuteTestCmd(message)
        
        if not await self.ExecuteCmd(msg_data.cmd.replace(Config.prefix, ""), message):
            return await message.channel.send("Failed to find command or corrupted Lib()")
    
    async def on_voice_state_update(self, member, before, after):
        # if before.channel != after.channel:
        #     # Check if the member joined or left a voice channel
        #     if after.channel:
        #         print(f'{member} joined voice channel {after.channel.name}.')
        #     elif before.channel:
        #         print(f'{member} left voice channel {before.channel.name}.')
        await self.ExecuteVcModerator("on_vc_event", member, before, after)
        # pass

c = DiscordCogs("src/commands/")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Networky(intents=intents, command_prefix={Config.prefix})
client.run('YOUR_TOKEN_HERE')