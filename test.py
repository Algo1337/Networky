import requests

from src.utils.str_utils import *

DATA_KEYS = [
    "IP address",
    "Host name",
    "IP range",
    "ISP",
    "Organization",
    "Country",
    "Region",
    "City",
    "Time zone",
    "Local time",
    "Postal Code"
]

req = requests.get("https://check-host.net/ip-info?host=8.8.8.8")

if req.status_code != 200:
    print("[ X ] Error, Something went wrong trying to connect to the API")
    exit(0)

resp = req.text
lines = resp.replace("<td class=\"break-all\">", "").replace("<td class=\"break-words\">", "").replace("</td>", "").replace("<strong>", "").replace("</strong>", "").split("\n")
i = 0
for line in lines:
    if i in [9, 32, 56]: continue
    if "ipinfo-item mb-3" in line: ## GEO API SERVER/BACKEND
        print(f"[{i}]: {lines[i + 4]}")

    for key in DATA_KEYS:
        if key in line:
            print(f"[{i}]: {lines[i + 1]}")
    i += 1