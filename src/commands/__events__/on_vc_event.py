import discord

async def on_voice_state_update(self, member, before, after):
    if before.channel != after.channel:  # Check if there was a change in voice channel
        if after.channel is None:  # User left a voice channel
            print(f'{member.display_name} left voice channel {before.channel.name}')
        elif before.channel is None:  # User joined a voice channel
            print(f'{member.display_name} joined voice channel {after.channel.name}')
        else:  # User switched voice channels
            print(f'{member.display_name} switched from {before.channel.name} to {after.channel.name}')

    # Check for mute and deafen events
    if before.self_mute != after.self_mute:
        if after.self_mute:
            print(f'{member.display_name} muted themselves in {after.channel.name}')
        else:
            print(f'{member.display_name} unmuted themselves in {after.channel.name}')
            
    if before.self_deaf != after.self_deaf:
        if after.self_deaf:
            print(f'{member.display_name} deafened themselves in {after.channel.name}')
        else:
            print(f'{member.display_name} undeafened themselves in {after.channel.name}')

    # Check for screenshare events
    if before.self_stream != after.self_stream:
        if after.self_stream:
            print(f'{member.display_name} started screensharing in {after.channel.name}')
        else:
            print(f'{member.display_name} stopped screensharing in {after.channel.name}')