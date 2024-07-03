import discord
import datetime

class BotInfo:
    def __init__(self, bot_version):
        self.start_time = datetime.datetime.now()
        self.bot_version = bot_version
    
    def get_uptime(self):
        current_time = datetime.datetime.now()
        uptime_delta = current_time - self.start_time
        return self.format_timedelta(uptime_delta)
    
    def get_version(self):
        return self.bot_version
    
    def format_timedelta(self, td):
        seconds = int(td.total_seconds())
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        if days > 0:
            return f'{days} days, {hours} hours, {minutes} minutes'
        elif hours > 0:
            return f'{hours} hours, {minutes} minutes'
        elif minutes > 0:
            return f'{minutes} minutes'
        else:
            return f'{seconds} seconds'

def generate_botinfo_embed(bot_version):
    bot_info = BotInfo(bot_version)
    embed = discord.Embed(title="Bot Information", color=0x7289DA)
    embed.add_field(name="Uptime", value=bot_info.get_uptime(), inline=False)
    embed.add_field(name="Version", value=bot_info.get_version(), inline=False)
    embed.set_footer(text="Command Made By VerSDK")
    return embed

# Example usage:
if __name__ == "__main__":
    bot_version = '1.0'  # Replace with your bot's actual version
    embed = generate_botinfo_embed(bot_version)
    print(embed.to_dict())  # Optional: Print embed as a dictionary for testing
