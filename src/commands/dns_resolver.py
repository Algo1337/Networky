from pydoc import resolve

import aiodns


async def resolve_dns(hostname):
    try:
        result = await resolve.query(hostname, 'A')
        ipv4_addresses = [response.host for response in result] if result else []

        result_v6 = await resolve.query(hostname, 'AAAA')
        ipv6_addresses = [response.host for response in result_v6] if result_v6 else []

        return ipv4_addresses, ipv6_addresses

    except aiodns.error.DNSError as e:
        print(f"DNS resolution failed for {hostname}: {e}")
        return [], []

    except Exception as e:
        print(f"An error occurred during DNS resolution for {hostname}: {e}")
        return [], []