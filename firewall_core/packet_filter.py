from scapy.all import sniff, IP, TCP, UDP, ICMP
from firewall_core.config import (
    BLOCKED_IPS, BLOCKED_PORTS, ALLOWED_PROTOCOLS, INTERFACE,
    WHITELISTED_IPS
)
from firewall_core.logger import log_event
from firewall_core.utils import get_protocol, extract_ports
from firewall_core.geo.geo import is_geo_blocked

def process_packet(packet):
    if not packet.haslayer(IP):
        return
    
    ip_src = packet[IP].src
    ip_dst = packet[IP].dst
    protocol = get_protocol(packet)
    port_src, port_dst = extract_ports(packet)

    # Whitelist check
    if ip_src in WHITELISTED_IPS:
        return

    # Blocked IPs
    if ip_src in BLOCKED_IPS or ip_dst in BLOCKED_IPS:
        log_event(f"Blocked IP: {ip_src} <-> {ip_dst}")
        return

    # Port blocking
    if port_src in BLOCKED_PORTS or port_dst in BLOCKED_PORTS:
        log_event(f"Blocked Port ({protocol}): {port_src} <-> {port_dst}")
        return

    # Protocol filtering
    if protocol not in ALLOWED_PROTOCOLS:
        log_event(f"Blocked Protocol: {protocol} from {ip_src}")
        return

    # Geo-blocking (optional)
    if is_geo_blocked(ip_src):
        log_event(f"Geo-blocked IP: {ip_src}")
        return

    # Else: Passed packet
    log_event(f"Allowed: {protocol} {ip_src}:{port_src} -> {ip_dst}:{port_dst}")

def start_packet_filter():
    sniff(prn=process_packet, store=0, iface=INTERFACE)
