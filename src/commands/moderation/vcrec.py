import discord

from discord.ext import commands, voice_recv

""" Not finished!  """
async def vcrec(message: discord.message):
    discord.opus.load_opus("/usr/lib/libopus.so.***")
    voice_client = await message.author.voice.channel.connect(cls=voice_recv.VoiceRecvClient)
    
    voice_client.listen(voice_recv.BasicSink(voice_callback))

    await message.channel.send('Started listening to voice data.')

def voice_callback(user, data: voice_recv.VoiceData):
    print(f"Got packet from {user}")