import json
import os
from scapy.all import get_if_list, get_working_if

CONFIG_PATH = "firewall_core/config.json"

BLOCKED_IPS = []
BLOCKED_PORTS = [23, 445, 135]
WHITELISTED_IPS = []
ALLOWED_PROTOCOLS = ['TCP', 'UDP', 'ICMP']
INTERFACE = None 

def validate_interface(name):
    return name in get_if_list()

if os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH) as f:
        data = json.load(f)
        BLOCKED_IPS = data.get("blocked_ips", BLOCKED_IPS)
        BLOCKED_PORTS = data.get("blocked_ports", BLOCKED_PORTS)
        WHITELISTED_IPS = data.get("whitelisted_ips", WHITELISTED_IPS)
        ALLOWED_PROTOCOLS = data.get("allowed_protocols", ALLOWED_PROTOCOLS)
        INTERFACE = data.get("interface")

if not INTERFACE or not validate_interface(INTERFACE):
    try:
        INTERFACE = get_working_if()
        print(f"[CONFIG] Using detected interface: {INTERFACE}")
    except Exception as e:
        print(f"[ERROR] No working network interface found: {e}")
        INTERFACE = None
