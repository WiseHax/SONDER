#  Sonder - Basic Python Firewall

**Sonder** is a basic Python-based firewall designed to block suspicious IPs, ports, and protocols. It can operate in monitor or active block mode, and is fully customizable through a configuration file.

>  This is a **basic-level project** and is not intended for production use. Advanced features like DPI, real-time packet inspection, and stateful filtering will be added in future versions.

---

##  Features

- Block specific IP addresses and ports  
- Allow only certain protocols (TCP, UDP, ICMP)  
- Whitelist trusted IPs  
- Monitor or actively block suspicious traffic  
- Easy configuration via `config.json`  
- Log activity to `firewall.log`  

---

##  Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/sonder-firewall.git
cd sonder-firewall
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create your own config

Copy the example config and customize it:

```bash
cp config.example.json config.json
```

Then edit `config.json` with your desired settings (example below):

```json
{
    "blocked_ips": ["x.x.x.x"],
    "blocked_ports": [23, 445, 135],
    "whitelisted_ips": ["x.x.x.x"],
    "allowed_protocols": ["TCP", "UDP", "ICMP"],
    "interface": "Wi-Fi"
}
```

###  How to Run

From your desktop directory (for example):

```bash
cd "%USERPROFILE%\OneDrive\Desktop\SONDER"
python run_firewall.py
```

The firewall will read from `config.json` and begin monitoring or blocking traffic based on your settings.

---

##  Configuration Reference (`config.json`)

| Key                | Description                        | Example                      |
|--------------------|------------------------------------|------------------------------|
| `blocked_ips`      | List of IPs to block               | `["192.168.1.100"]`          |
| `blocked_ports`    | List of ports to block             | `[23, 445, 135]`             |
| `whitelisted_ips`  | Bypass filter for specific IPs     | `["127.0.0.1"]`              |
| `allowed_protocols`| Allowed protocols only (optional)  | `["TCP", "UDP"]`             |
| `interface`        | Network interface to monitor       | `"Wi-Fi"` or `"Ethernet"`    |

---

##  License

MIT License

Copyright (c) 2025 [ WXSE ]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY...


---

##  Notes

- Make sure to run the script with admin/root privileges to access raw sockets.
- Only works on systems that support Python raw socket manipulation (Linux, Windows).
- Tested on Python 3.10+.

---

##  Coming Soon

- DPI (Deep Packet Inspection)
- Real-time visualization dashboard
- GeoIP filtering
- Stateful inspection engine
- Web GUI and remote control panel
