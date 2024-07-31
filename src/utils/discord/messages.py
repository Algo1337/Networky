"""
    [ Custom Discord Message Utility Sub-Module ]
"""
import discord 

from discord import Embed

class MsgInfo():
    data:   str;
    cmd:    str;
    args:   str;

class Message():
    info:   MsgInfo;
    def __init__(self, message: discord.message):
        self.info   = MsgInfo()
        self.data, self.cmd = message.content, message.content
        self.args = []
        
        if " " in self.data:
            self.args = self.data.split(" ")
            self.cmd = self.args[0]

    @staticmethod
    async def SendEmbedMsg(message: discord.message, t: str, desc: str, fields: dict[str, str]) -> bool:
        embed = Embed(title = t, description = desc)

        if len(fields) > 0:
            for field in fields:
                embed.add_field(name = field, value = fields[field], inline = False)

        await message.channel.send(embed=embed)
