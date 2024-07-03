"""
    [ Check Host API Client ]

    @title: Check Host SDK
    @author: @Algorithm1337
    @since: 7/2/24
    @github: github.com/AdvancedAlgorithm
"""
import requests, json

from ..utils.net_checks import *

Checkhost_API = "https://check-host.net/check-tcp?host="

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

        resp = requests.get(f"{Checkhost_API}{ip}&max_nodes={self.nodes}", headers={"Accept": "application/json"})
        
        if resp.status_code != 200:
            print(f"[ X ] Error, Something went wrong connecting to Check host's API....!")
            return Response()
        
        json_data = json.loads(resp.text)

        for key in json_data["nodes"]:
            val = json_data["nodes"][key]
            print(f"{key} = {val}")
        
api = CheckHostSDK(5)
search = api.TCPPing("70.70.70.72")