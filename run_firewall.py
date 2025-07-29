import os
import threading
import time
from pystyle import Colors, Colorate, Center, Write
from firewall_core.packet_filter import start_packet_filter
from firewall_core.logger import log_event
from firewall_core import config

BANNER = """
░██████╗░█████╗░███╗░░██╗██████╗░███████╗██████╗░
██╔════╝██╔══██╗████╗░██║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██║░░██║██╔██╗██║██║░░██║█████╗░░██████╔╝
░╚═══██╗██║░░██║██║╚████║██║░░██║██╔══╝░░██╔══██╗
██████╔╝╚█████╔╝██║░╚███║██████╔╝███████╗██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝
"""

def show_config():
    print(Colorate.Horizontal(Colors.red_to_white, "\n[CONFIG] Loaded Configuration:"))
    print(f" - Interface: {config.INTERFACE}")
    print(f" - Blocked IPs: {config.BLOCKED_IPS}")
    print(f" - Blocked Ports: {config.BLOCKED_PORTS}")
    print(f" - Whitelisted IPs: {config.WHITELISTED_IPS}")
    print(f" - Allowed Protocols: {config.ALLOWED_PROTOCOLS}\n")

def show_logs():
    log_path = "firewall_core/firewall.log"
    print(Colorate.Horizontal(Colors.red_to_white, "\n[LOGS] Last 10 events:\n"))
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            lines = f.readlines()[-10:]
            for line in lines:
                print("  " + line.strip())
    else:
        print("  No log file found.\n")

def main_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        
        print(Colorate.Vertical(Colors.red_to_white, Center.XCenter(BANNER)))

        print(Colorate.Horizontal(Colors.red_to_white, """
[ MENU ]
   [1] Start Firewall
   [2] View Logs
   [3] Show Config
   [4] Exit
        """.rstrip()))

        choice = input(Colorate.Horizontal(Colors.red_to_white, "\n>> Choose option: ")).strip()

        if choice == "1":
            try:
                from firewall_core.firewall import start_firewall
                start_firewall()
            except Exception as e:
                print(Colorate.Horizontal(Colors.red_to_white, f"\n[ERROR] Failed to start firewall: {e}"))
                input("Press Enter to return...")
        elif choice == "2":
            show_logs()
            input("\nPress Enter to return to menu...")
        elif choice == "3":
            show_config()
            input("\nPress Enter to return to menu...")
        elif choice == "4":
            print(Colorate.Horizontal(Colors.green_to_white, "\nExiting firewall... BYE NIGGA"))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_white, "\nInvalid option!"))
            input("Press Enter to try again...")

if __name__ == "__main__":
    main_menu()
