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
    class Route:
        NONE:       int = 0x000000
        PING_ICMP:  int = 0x100001
        PING_TCP:   int = 0x100002
        HTTP_PING:  int = 0x100003
        DNS_PING:   int = 0x100004
    
class PingResults():
    COUNTRY_INITIAL:    str = "";
    COUNTRY_STATE:      str = "";
    COUNTRY_NAME:       str = "";
    IP_ADDRESS:         str = "";
    ASN:                str = "";
    HOSTNAME:           str = "";
    RESPONSE_TIME:      str = "";
    def __init__(self, ctry_i: str, ctry_state: str, ctry_name: str, ip_addr: str, asn: str, hostname: str):
        self.COUNTRY_INITIAL = ctry_i; self.COUNTRY_STATE = ctry_state;
        self.COUNTRY_NAME = ctry_name; self.IP_ADDRESS = ip_addr;
        self.ASN = asn; self.HOSTNAME = hostname;

        

class CheckHostSDK():
    nodes:  int = 0;
    def __init__(self, max_nodes: int) -> None:
        self.nodes = max_nodes

    def TCPPing(self, ip: str) -> str:
        if not validate_ipv4_format(ip):
            print(f"[ X ] Error, An invalid IP Address was provided!")
            return False

        resp = requests.get(f"{CheckHostAPI.url}{ip}&max_nodes={self.nodes}", headers={"Accept": "application/json"})
        if resp.status_code != 200:
            return ""
        
        json_data = json.loads(resp.text)

        results = {}
        for k in json_data["nodes"]:
            results[k] = PingResults(
                json_data["nodes"][k][0], json_data["nodes"][k][1], json_data["nodes"][k][2],
                json_data["nodes"][k][3], json_data["nodes"][k][4], k
            )

        reqid = json_data['request_id']
        time.sleep(1.3)

        response = requests.get(f"https://check-host.net/check-result/{reqid}", headers={"Accept": "application/json"})
        if response.status_code != 200:
            return ""
        
        data = ""
        ping_results = response.json()
        for key in ping_results:
            if isinstance(ping_results[k], list):
                if "time" in ping_results[k][0]:
                    results[key].TIME = ping_results[k][0]["time"]
                else:
                    results[key].TIME = "N/A"
            
            # results[k].RESPONSE_TIME = ping_results[k][0]
        
        return results