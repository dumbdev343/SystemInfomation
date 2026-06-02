#!/bin/bash

clear

echo "Downloading the script"

cd /tmp

curl -LO https://raw.githubusercontent.com/dumbdev343/SystemInformation/refs/heads/main/main.py 

echo "Installing to the /usr/bin directory (may require sudo)"

sudo install -Dm755 /tmp/main.py /usr/bin/systeminfo

chmod +x /usr/bin/systeminfo

echo "Done! Run systeminfo in a terminal to get started!"



