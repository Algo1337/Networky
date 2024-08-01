import discord

async def on_vc_event(member, before = None, after = None):
    if before.channel != after.channel:
        # Check if the member joined or left a voice channel
        if after.channel:
            print(f'[ + ] {member} joined voice channel #{after.channel.name}.')
        elif before.channel:
            print(f'[ + ] {member} left voice channel #{before.channel.name}.')

    # Check for mute and deafen events
    if before.self_mute != after.self_mute:
        if after.self_mute:
            print(f'[ + ] {member.display_name} muted themselves in #{after.channel.name}')
        else:
            print(f'[ + ] {member.display_name} unmuted themselves in #{after.channel.name}')
            
    if before.self_deaf != after.self_deaf:
        if after.self_deaf:
            print(f'[ + ] {member.display_name} deafened themselves in #{after.channel.name}')
        else:
            print(f'[ + ] {member.display_name} undeafened themselves in #{after.channel.name}')

    # Check for screenshare events
    if before.self_stream != after.self_stream:
        if after.self_stream:
            print(f'[ + ] {member.display_name} started screensharing in #{after.channel.name}')
        else:
            print(f'[ + ] {member.display_name} stopped screensharing in #{after.channel.name}')