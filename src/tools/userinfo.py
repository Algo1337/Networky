# userinfo.py

import discord
from discord.ext import commands

class UserInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def lookup(self, ctx, member: discord.Member):
        # Fetches member information
        embed = discord.Embed(title="User Look-up Results", color=discord.Color.blue())
        embed.set_author(name=member.display_name, icon_url=member.avatar_url)
        embed.add_field(name="Username", value=member.name, inline=False)
        embed.add_field(name="Discriminator", value=member.discriminator, inline=False)
        embed.add_field(name="ID", value=member.id, inline=False)
        embed.add_field(name="Joined Server", value=member.joined_at.strftime("%Y-%m-%d %H:%M:%S"), inline=False)
        embed.set_footer(text="Command made by VerSDK")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(UserInfo(bot))
