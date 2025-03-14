#!/usr/bin/env bash

# Warna
RED='\033[1;31m'
GREEN='\033[1;32m'
WHITE='\033[1;37m'
NC='\033[0m' # Reset Warna

# Tampilan Header
clear
echo -e "${RED}===================================="
echo -e "         S-OXVA INSTALLER          "
echo -e "====================================${NC}"

# Cek & Instal Python2 jika belum ada
if ! command -v python2 &> /dev/null
then
    echo -e "${WHITE}[INFO] Python2 not found, installing...${NC}"
    pkg install python2 -y
else
    echo -e "${GREEN}[OK] Python2 is already installed.${NC}"
fi

# Instal paket pendukung
echo -e "${WHITE}[INFO] Installing dependencies...${NC}"
pkg install git -y
pkg install jq -y

# Unduh script S-OXVA.py dari GitHub
echo -e "${WHITE}[INFO] Downloading S-OXVA script...${NC}"
curl -o S-OXVA.py https://raw.githubusercontent.com/NABZEid/S-OXVA/main/S-OXVA.py
chmod +x S-OXVA.py

# Selesai & Jalankan Script
echo -e "${GREEN}[SUCCESS] Installation complete!${NC}"
echo -e "${WHITE}[INFO] Run the script using: ${GREEN}python2 S-OXVA.py${NC}"
