import discord 
"""
    [ Custom Discord Message Utility Sub-Module ]
"""

class MsgInfo():
    data:   str;
    cmd:    str;
    args:   str;

class Message():
    info:   MsgInfo;
    def __init__(self, message):
        self.info   = MsgInfo()
        self.data, self.cmd, self.args = message.content, message.content, [message.content]
        
        if " " in self.data:
            self.args = self.data.split(" ")
            self.cmd = self.args[0]