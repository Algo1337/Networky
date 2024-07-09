
from ..tools.check_host import *

async def ch(message):
    api = CheckHostSDK(25)
    search = api.TCPPing("70.70.70.72")
    await message.channel.send(search)