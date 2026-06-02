import os
import time
import platform
import cpuinfo 
import pygame
import sys
import random
pygame.init()
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),)
font = pygame.font.SysFont(None, 36)
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("System Infomation")
assci = r"""
  ___         _               ___       __                    _   _          
 / __|_  _ __| |_ ___ _ __   |_ _|_ _  / _|___ _ _ _ __  __ _| |_(_)___ _ _  
 \__ \ || (_-<  _/ -_) '  \   | || ' \|  _/ _ \ '_| '  \/ _` |  _| / _ \ ' \ 
 |___/\_, /__/\__\___|_|_|_| |___|_||_|_| \___/_| |_|_|_\__,_|\__|_\___/_||_|
      |__/                                                                                                                                                
"""
font.render(f"You are running {platform.system()}!", True, (128, 253, 123), (0, 0, 0))

os.system("clear")
print(assci)
if platform.system() == ("Windows"):
    print("You are running on Windows!")
if platform.system() == ("Linux"):
    print("You are running on Linux!")
    if os.path.exists("/etc/debian_version"):
        print("You are running on the Distro Debian!")
if platform.system() == ("Darwin"):
    print("You are running on Darwin/Linux!")
print(f"Your CPU is the {cpuinfo.get_cpu_info()["brand_raw"]} and it has {os.cpu_count()} cores!")
screen.fill("white")
pygame.display.flip()
print(" ")
print(" ")

install = input("Would you like to install any programs? ")
if "yes" in install:
    if platform.system() == ("Windows"):
        pkgname = input("What package would you like to install? (Using WinGet): ")
        os.system(f"winget install {pkgname}")

