from pydoc import resolve

async def resolve_dns(message):
    await message.channel.send("What DNS do you want to resolve?");