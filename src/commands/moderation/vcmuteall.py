import discord

async def vcmuteall(ctx):
    if not ctx.author.guild_permissions.administrator:
        embed = discord.Embed(
            title="Permission Denied 🚫",
            description="You do not have permission to manage roles 🚫.",
            color=discord.Color.red()
        )
        return await ctx.send(embed=embed)
    
    if not ctx.author.voice:
        embed = discord.Embed(
            title="Not Connected ⚠️!",
            description="You are not connected to a voice channel ⚠️!",
            color=discord.Color.red()
        )
        return await ctx.send(embed=embed)
    
    voice_channel = ctx.author.voice.channel

    for member in voice_channel.members:
        await member.edit(mute=True)
        embed = discord.Embed(
            title="User Muted 🔈",
            description=f"{member.display_name} has been server muted ⚙️.",
            color=discord.Color.green()
        )
        await ctx.send(embed=embed)