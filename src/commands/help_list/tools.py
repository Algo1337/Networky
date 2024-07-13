import discord

from discord import message

async def tools(message: discord.message) -> bool:
    files = os.listdir("src/commands/tools/")
    # Construct an Embed Msg
    embed = Embed(title="Help", description="List of Commands", color=discord.Color.green())
    for cmd in files:
        if os.path.isfile(cmd):
            embed.add_field(name=cmd, value=f"{Config.prefix}{cmd}", inline=False)

    await message.channel.send(embed=embed)