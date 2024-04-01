#!/usr/bin/env python3
import os
import platform
import psutil

# Variable
private_ip = (os.popen("ifconfig|awk ' /inet / && /broadcast/ {print $2 } '").read().strip())

disk = psutil.disk_usage('/')
root_total = format(disk.total/1024**3,".1f")
root_used = format(disk.used/1024**3,".1f")

# General
print("Hostname: ", os.popen("hostname").read().strip())
print("Kernel:" ,platform.system())
# Using uptime instead, psutil boot_time() is hard parse, will use fully awk instead of cut
print("Uptime:", os.popen("uptime| awk -F ',' '{print $1}'|awk -F 'up' '{ print $2 }'|sed 's/ //g'").read().strip())
print("CPU (%):", psutil.cpu_percent(0.5))
print("Mem Used (GB):", format(psutil.virtual_memory()[3]/1024**3, ".1f"),"/",format(psutil.virtual_memory()[0]/1024**3,".1f"))

# Network
print("Private IP:", private_ip)

# Will add conditioin where condition where it'll use wget, not all system have curl
print("Public IP:", os.popen("curl -s ifconfig.me").read().strip())

# Disk
print("Disk Usage '/' (GB):",root_used,"/",root_total)

# Last Update



