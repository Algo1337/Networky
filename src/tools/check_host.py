"""
    [ Check Host API Client ]

    @title: Check Host SDK
    @author: @Algorithm1337
    @since: 7/2/24
    @github: github.com/AdvancedAlgorithm
"""
import requests, json, enum, time

from dataclasses import dataclass

from ..utils.net_checks import *

class CheckHostAPI():
    url = "https://check-host.net/check-tcp?host="
    routes = {
        "PING_ICMP": "check-ping",
        "PING_TCP": "check-tcp",
        "HTTP_PING": "check-http",
        "DNS_PING": "check-dns"
    }
    class Route:
        NONE:       int = 0x000000
        PING_ICMP:  int = 0x100001
        PING_TCP:   int = 0x100002
        HTTP_PING:  int = 0x100003
        DNS_PING:   int = 0x100004

class Response():
    pass

class CheckHostSDK():
    nodes:  int = 0;
    def __init__(self, max_nodes: int) -> None:
        self.nodes = max_nodes

    def TCPPing(self, ip: str) -> Response:
        if not validate_ipv4_format(ip):
            print(f"[ X ] Error, An invalid IP Address was provided!")
            return False

        resp = requests.get(f"{CheckHostAPI.url}{ip}&max_nodes={self.nodes}", headers={"Accept": "application/json"})
        if resp.status_code != 200:
            return ""
        
        json_data = json.loads(resp.text)
        reqid = json_data['request_id']

        time.sleep(1.3)

        response = requests.get(f"https://check-host.net/check-result/{reqid}", headers={"Accept": "application/json"})
        if response.status_code != 200:
            return ""
        
        data = ""
        ping_results = response.json()
        for key in ping_results:
            val = ping_results[key]
            data += f"{key}: {val}\n";
        
        return data