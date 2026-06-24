#!/bin/bash

echo "💀 Starting WebInfo Setup..."

# Detect Environment

if [[ "$PREFIX" == *"com.termux"* ]]; then
echo "[*] Detected: Termux"

```
pkg update -y && pkg upgrade -y

pkg install -y python git curl whois
```

elif [[ -f "/etc/debian_version" ]]; then
echo "[*] Detected: Debian/Ubuntu/Kali"

```
sudo apt update -y && sudo apt upgrade -y

sudo apt install -y python3 python3-pip git curl whois
```

else
echo "[!] Unsupported OS"
exit 1
fi

echo "[*] Installing Python modules..."

pip3 install --upgrade pip
pip3 install requests colorama python-whois dnspython

echo "[✓] All dependencies installed successfully!"

echo ""
echo "👉 Now run your tool:"
echo "python3 WebInfo.py"
