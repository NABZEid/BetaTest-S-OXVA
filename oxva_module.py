# oxva_module.py - Module untuk S-OXVA

import os
import requests

# Warna ANSI untuk tampilan di Terminal
RED = '\033[1;31m'
GREEN = '\033[1;32m'
WHITE = '\033[1;37m'
NC = '\033[0m'  # Reset Warna

def tampilkan_header():
    """ Menampilkan Header Program """
    os.system("clear")
    print(f"{RED}====================================")
    print("         S-OXVA MODULE LOADED       ")
    print(f"===================================={NC}")

def cek_koneksi():
    """ Mengecek Koneksi Internet """
    try:
        requests.get("https://www.google.com", timeout=3)
        print(f"{GREEN}[OK] Internet Connection Active.{NC}")
        return True
    except requests.ConnectionError:
        print(f"{RED}[ERROR] No Internet Connection.{NC}")
        return False
