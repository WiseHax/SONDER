from scapy.layers.inet import TCP, UDP, ICMP

def get_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    return "OTHER"

def extract_ports(packet):
    sport = dport = None
    if packet.haslayer(TCP) or packet.haslayer(UDP):
        sport = packet.sport
        dport = packet.dport
    return sport, dport
