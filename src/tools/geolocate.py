# geolocate.py

import discord
from discord.ext import commands
from geopy.geocoders import Nominatim

class Geolocation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.geolocator = Nominatim(user_agent="discord-bot")

    @commands.command()
    async def geolocate(self, ctx, *, location):
        try:
            # Attempt to geolocate the given location
            location = self.geolocator.geocode(location)

            if location:
                embed = discord.Embed(title="Geolocation", color=discord.Color.blue())
                embed.add_field(name="Location", value=location.address, inline=False)
                embed.add_field(name="Latitude", value=location.latitude, inline=True)
                embed.add_field(name="Longitude", value=location.longitude, inline=True)
                embed.set_footer(text="Geolocation provided by Nominatim | Command Made By VerSDK")

                await ctx.send(embed=embed)
            else:
                await ctx.send("Location was unable to be located. Please Check For Errors.")
        
        except Exception as e:
            await ctx.send(f"Error occurred: {str(e)}")

def setup(bot):
    bot.add_cog(Geolocation(bot))
