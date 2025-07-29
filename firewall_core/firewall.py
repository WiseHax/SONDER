from firewall_core.packet_filter import start_packet_filter
from firewall_core.logger import log_event

def start_firewall():
    log_event("[FIREWALL] Starting packet filter...")
    start_packet_filter()
