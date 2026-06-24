import subprocess
import sys

required_modules = {
    "requests": "requests",
    "whois": "python-whois",
    "colorama": "colorama"
}

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for module, package in required_modules.items():
    try:
        __import__(module)
    except ImportError:
        print(f"[+] Installing {package}...")
        install(package)
        
import socket
import requests
import whois
import os
from colorama import Fore, init

init(autoreset=True)

results = []

# -------- UI --------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def banner():
    clear()
    print(Fore.GREEN + r"""

__        __   _     ___        __       
\ \      / /__| |__ |_ _|_ __  / _| ___  
 \ \ /\ / / _ \ '_ \ | || '_ \| |_ / _ \ 
  \ V  V /  __/ |_) || || | | |  _| (_) |
   \_/\_/ \___|_.__/|___|_| |_|_|  \___/ 

+------------------------------------------------------+
|        ADVANCED WEB INFORMATION GATHERING TOOL       |
+------------------------------------------------------+

        [ ARGRecon - WebInfo PRO Toolkit ]

+------------------------------------------------------+
|  Developed By : ARGCyberSkillHub                     |
|  Website      : https://argskillhub.com              |
|  Status       : STAY LEGAL | STAY ETHICAL            |
+------------------------------------------------------+

""")

# -------- SAVE --------
def save_results():
    with open("results.txt", "w", encoding="utf-8") as f:
        for line in results:
            f.write(line + "\n")
    print(Fore.GREEN + "[+] Results saved to results.txt")

# -------- IP INFO --------
def ip_lookup():
    ip = input(Fore.YELLOW + "\n[?] Enter IP: ")

    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()

        print(Fore.GREEN + "\n[+] IP Info:\n")

        keys = ["query","country","regionName","city","zip","isp","org","timezone"]
        for k in keys:
            val = data.get(k, "N/A")
            line = f"{k}: {val}"
            print(Fore.CYAN + line)
            results.append(line)

        print(Fore.YELLOW + f"\n[MAP] https://maps.google.com/?q={data.get('lat')},{data.get('lon')}")

    except:
        print(Fore.RED + "[!] Failed")

# -------- DNS --------
def dns_lookup():
    domain = input(Fore.YELLOW + "\n[?] Domain: ")

    try:
        print(Fore.GREEN + "\n[+] DNS Info:\n")

        ip = socket.gethostbyname(domain)
        print(Fore.CYAN + f"A Record: {ip}")
        results.append(f"A Record: {ip}")

        print(Fore.CYAN + "\nMX Records:")
        mx = socket.getaddrinfo(domain, None)
        for m in mx:
            line = f"MX: {m[4][0]}"
            print(" ", line)
            results.append(line)

        print(Fore.CYAN + "\nNS Records:")
        ns = socket.gethostbyname_ex(domain)
        for n in ns[2]:
            line = f"NS: {n}"
            print(" ", line)
            results.append(line)

    except:
        print(Fore.RED + "[!] DNS Failed")

# -------- WHOIS --------
def whois_lookup():
    domain = input(Fore.YELLOW + "\n[?] Domain: ")

    try:
        info = whois.whois(domain)

        print(Fore.GREEN + "\n[+] WHOIS:\n")

        keys = ["domain_name","registrar","creation_date","expiration_date","name_servers"]
        for k in keys:
            val = info.get(k, "N/A")
            line = f"{k}: {val}"
            print(Fore.CYAN + line)
            results.append(line)

    except:
        print(Fore.RED + "[!] WHOIS Failed")

# -------- PORT SCAN --------
def port_scan():
    target = input(Fore.YELLOW + "\n[?] Target IP: ")
    ports = [21,22,25,53,80,110,139,143,443,445,3306,3389,8080]

    print(Fore.GREEN + "\n[*] Scanning ports...\n")

    for port in ports:
        s = socket.socket()
        s.settimeout(0.8)

        if s.connect_ex((target, port)) == 0:
            line = f"[+] Port {port} OPEN"
            print(Fore.GREEN + line)
            results.append(line)
        else:
            print(Fore.RED + f"[-] Port {port} CLOSED")

        s.close()

# -------- SUBDOMAIN --------
def subdomain_scan():
    domain = input(Fore.YELLOW + "\n[?] Domain: ")
    subs = ["www","mail","ftp","api","dev","test","blog"]

    print(Fore.GREEN + "\n[*] Finding subdomains...\n")

    for sub in subs:
        url = f"{sub}.{domain}"
        try:
            ip = socket.gethostbyname(url)
            line = f"[+] {url} -> {ip}"
            print(Fore.GREEN + line)
            results.append(line)
        except:
            print(Fore.RED + f"[-] {url}")

# -------- MENU --------
def menu():
    while True:
        print(Fore.CYAN + """
==============================
[1] IP Lookup
[2] DNS Lookup
[3] WHOIS Lookup
[4] Port Scan
[5] Subdomain Scan
[6] Save Results
[7] Exit
==============================
""")

        choice = input(Fore.GREEN + "ARGRecon > ")

        if choice == "1":
            ip_lookup()
        elif choice == "2":
            dns_lookup()
        elif choice == "3":
            whois_lookup()
        elif choice == "4":
            port_scan()
        elif choice == "5":
            subdomain_scan()
        elif choice == "6":
            save_results()
        elif choice == "7":
            break
        else:
            print(Fore.RED + "Invalid")

        input("\nPress Enter...")
        banner()

# -------- MAIN --------
if __name__ == "__main__":
    banner()
    menu()
