from pydoc import resolve


import discord
from discord.ext import commands
import aiodns

class DNSResolver(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.resolver = aiodns.DNSResolver()

    async def resolve_dns(self, hostname):
        try:
            result = await self.resolver.query(hostname, 'A')
            ipv4_addresses = [response.host for response in result] if result else []

            result_v6 = await self.resolver.query(hostname, 'AAAA')
            ipv6_addresses = [response.host for response in result_v6] if result_v6 else []

            return ipv4_addresses, ipv6_addresses

        except aiodns.error.DNSError as e:
            print(f"DNS resolution failed for {hostname}: {e}")
            return [], []

        except Exception as e:
            print(f"An error occurred during DNS resolution for {hostname}: {e}")
            return [], []

    @commands.command(name='DNSResolver')
    async def dns_resolver_command(self, ctx, hostname):
        ipv4_addresses, ipv6_addresses = await self.resolve_dns(hostname)

        ipv4_str = "\n".join(ipv4_addresses) if ipv4_addresses else "No IPv4 addresses found."
        ipv6_str = "\n".join(ipv6_addresses) if ipv6_addresses else "No IPv6 addresses found."

        response = f"DNS Resolution Results for {hostname}:\n\nIPv4 Addresses:\n{ipv4_str}\n\nIPv6 Addresses:\n{ipv6_str}"
        await ctx.send(response)

def setup(bot):
    bot.add_cog(DNSResolver(bot))
