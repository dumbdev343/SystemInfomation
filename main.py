import os
import time
import platform
import cpuinfo 
import sys
import random

ascii = r'''
  ___         _               ___       __                    _   _          
 / __|_  _ __| |_ ___ _ __   |_ _|_ _  / _|___ _ _ _ __  __ _| |_(_)___ _ _  
 \__ \ || (_-<  _/ -_) '  \   | || ' \|  _/ _ \ '_| '  \/ _` |  _| / _ \ ' \ 
 |___/\_, /__/\__\___|_|_|_| |___|_||_|_| \___/_| |_|_|_\__,_|\__|_\___/_||_|
      |__/                                                                   
'''

cpu = cpuinfo.get_cpu_info()["brand_raw"]

if platform.system() == "Windows":
    os.system("cls")
else :
    os.system("clear")
print(ascii)

print(f"You are running on {platform.system()}!)")
print(f"Your CPU is the {cpu} and has {os.cpu_count()} cores!")

if platform.system() == ("Linux"):
    if os.path.exists("/etc/debian_version"):
        print("You are running on Debian Linux!")



print(" ")
print(" ")



        
