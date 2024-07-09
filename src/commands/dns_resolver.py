from pydoc import resolve

async def dns_resolver(message):
    await message.channel.send("What DNS do you want to resolve?");