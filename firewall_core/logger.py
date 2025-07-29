import os
from datetime import datetime

LOG_PATH = "firewall_core/firewall.log"

def log_event(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_PATH, "a") as f:
        f.write(entry + "\n")
