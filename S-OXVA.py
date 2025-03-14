#!/usr/bin/env python2

import os
import urllib2
import json

# Warna
RED = "\033[1;31m"
WHITE = "\033[1;37m"
CYAN = "\033[1;36m"
GREEN = "\033[1;32m"
NC = "\033[0m"  # Reset warna

# Tampilan Header
os.system("clear")
print(RED + "====================================")
print("         S-OXVA BETA TESTER        ")
print("====================================" + NC)
print(WHITE + "DEVELOPER          : [$]" + NC)
print(WHITE + "VERSION            : [$]" + NC)
print(WHITE + "TOTAL FEATURE      : [$]" + NC)
print(WHITE + "RUN                : [$]" + NC + "\n")

# Menu
print(CYAN + "[1]" + WHITE + " To trace target IP.")
print(CYAN + "[2]" + WHITE + " To trace your own IP.")
print(CYAN + "[3]" + WHITE + " To show help.")
print(CYAN + "[4]" + WHITE + " To update ip-tracer.")
print(CYAN + "[5]" + WHITE + " To start ip-tracer menu.")
print(CYAN + "[0]" + WHITE + " Exit.\n")

# Input Pilihan
option = raw_input("Choose an option: ")

if option == "1":
    target_ip = raw_input("Enter target IP: ")
    response = urllib2.urlopen("http://ip-api.com/json/" + target_ip)
    data = json.load(response)
    print(json.dumps(data, indent=4))

elif option == "2":
    response = urllib2.urlopen("http://ip-api.com/json")
    data = json.load(response)
    print(json.dumps(data, indent=4))

elif option == "3":
    print(GREEN + "Usage:")
    print("  - Option 1: Enter a target IP to trace.")
    print("  - Option 2: Show your own IP details.")
    print("  - Option 3: Show help menu.")
    print("  - Option 4: Update ip-tracer tool.")
    print("  - Option 5: Open ip-tracer menu.")
    print("  - Option 0: Exit script.")
    print(NC)

elif option == "4":
    print(GREEN + "Updating ip-tracer..." + NC)
    os.system("pkg update && pkg upgrade -y")

elif option == "5":
    print(GREEN + "Starting ip-tracer menu..." + NC)
    os.system("pkg install git -y && git clone https://github.com/rajkumardusad/IP-Tracer.git && cd IP-Tracer && bash ip-tracer")

elif option == "0":
    print(RED + "Exiting..." + NC)

else:
    print(RED + "Invalid option!" + NC)
