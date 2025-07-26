#!/usr/bin/env python3

import platform
import distro
import cpuinfo
#import amdsmi
import socket
import psutil
import os
import sys


logo = [
    " .oooo.",
    "o   o  o",
    "ooooo  oo",
    "o      oo",
    " 'oooooooooooo.",
    "       oo      o",
    "       oo  ooooo",
    "        o  o   o",
    "         'oooo'"
]

#set up everything

hostname_name = socket.gethostname()
kernel_ver = os.uname()[2]
os_name = platform.system()
os_distro = distro.id()
cpu_info = cpuinfo.get_cpu_info()
cpu_arch = platform.processor()
cpu_brand = cpu_info['brand_raw']  
wm_name = os.environ.get("XDG_CURRENT_DESKTOP")  
shell_name = os.environ.get("SHELL")
ram_info = psutil.virtual_memory()  
total_ram = ram_info.total  
percent_ram = ram_info.percent  
  
swap_info = psutil.swap_memory()  
total_swap = swap_info.total  
percent_swap = swap_info.percent

# get the info, GPU is hardcoded cause UGGHHHHH
info_lines = [
    f"Hostname: {hostname_name}",
    f"Kernel: {kernel_ver}",
    f"Platform: {os_name}",
    f"Distro: {os_distro}",
    f"CPU: {cpu_brand} {cpu_arch}",
    "GPU: RX 7800 XT",
    f"WM: {wm_name}",
    f"Shell: {shell_name[5:]}",
    f"RAM: {total_ram / (1024**3):.2f} GB",
    f"RAM Used: {percent_ram}%",
    f"Swap: {total_swap / (1024**3):.2f} GB",
    f"Swap Used: {percent_swap}%"
]

# Print logo
max_lines = max(len(logo), len(info_lines))
for i in range(max_lines):
    logo_line = logo[i] if i < len(logo) else " " * 20
    info_line = info_lines[i] if i < len(info_lines) else ""
    print(f"{logo_line:<20} {info_line}")
