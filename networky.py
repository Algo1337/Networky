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
            await self.ExecuteCmd("on_msg_event", message)

        if not msg_data.data.startswith(Config.prefix):
            return
        
        if not await self.ExecuteCmd(msg_data.args[0].replace(Config.prefix, ""), message):
            return await message.channel.send("Failed to find command or corrupted Lib()")

        print(f'[ + ] Message from {message.author}: {message.content}')
    
    async def on_voice_state_update(self, member, before, after):
        # This event is triggered whenever a member's voice state changes (e.g., joining, leaving, moving channels)
        if before.channel != after.channel:
            # Check if the member joined or left a voice channel
            if after.channel:
                print(f'{member} joined voice channel {after.channel.name}.')
            elif before.channel:
                print(f'{member} left voice channel {before.channel.name}.')

c = DiscordCogs("src/commands/")
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = Networky(intents=intents, command_prefix={Config.prefix})



























client.run('MTI0Njk3ODcxMjI5ODE5MjkzNw.Gtdx1q.ntbXI4KoR2CcHDtFZTXCOyGuALke3rwoGUIdvU')