#!/usr/bin/env python3

# Libraries
import random


# Colors
black='\033[1;90m'      # Black
red='\033[1;91m'        # Red
green='\033[1;92m'      # Green
yellow='\033[1;93m'     # Yellow
blue='\033[1;94m'       # Blue
purple='\033[1;95m'     # Purple
cyan='\033[1;96m'       # Cyan
white='\033[1;97m'      # White
reset='\033[0m'         # Reset
flash='\033[5m'         # Flash

# Logo
logo = (f"""

{flash}{green}███████╗██████╗  █████╗ ███╗   ███╗  {blue}  ██████╗ ██╗   ██╗
{flash}{green}██╔════╝██╔══██╗██╔══██╗████╗ ████║  {blue}  ██╔══██╗╚██╗ ██╔╝
{flash}{white}███████╗██████╔╝███████║██╔████╔██║  {blue}  ██████╔╝ ╚████╔╝ 
{flash}{white}╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║  {blue}  ██╔═══╝   ╚██╔╝  
{flash}{red}███████║██║     ██║  ██║██║ ╚═╝ ██║  {blue}  ██║        ██║   
{flash}{red}╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  {blue}  ╚═╝        ╚═╝   
{reset}                                                        
""")

# user agents
user_agents = [
    "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0",
    "Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15",
    "Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko",
    "Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16",
    "Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025",
    "Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1",
    "Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1",
    "Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)"
]

# Tor proxy
# proxy = {
#     'http': 'socks5://localhost:9050',
#     'https': 'socks5://localhost:9050'
# }

# other proxies
proxy = {
    'socks5' : '192.111.137.37:18762'
}

# Headers
SnappHeader = {
    "Host": "app.snapp.taxi", 
    "content-length": "29", 
    "x-app-name": "passenger-pwa", 
    "x-app-version": "5.0.0", 
    "app-version": "pwa", 
    "user-agent": "".join(random.choices(user_agents)), 
    "content-type": "application/json", 
    "accept": "*/*", "origin": "https://app.snapp.taxi", 
    "sec-fetch-site": "same-origin", 
    "sec-fetch-mode": "cors", 
    "sec-fetch-dest": "empty", 
    "referer": "https://app.snapp.taxi/login/?redirect_to\u003d%2F", 
    "accept-encoding": "gzip, deflate, br", 
    "accept-language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6", 
    "cookie": "_gat\u003d1"
}


GapHeader = {
    "Host": "core.gap.im",
    "accept": "application/json, text/plain, */*",
    "x-version": "4.5.7",
    "accept-language": "fa",
    "user-agent": "".join(random.choices(user_agents)),
    "appversion": "web",
    "origin": "https://web.gap.im",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://web.gap.im/",
    "accept-encoding": "gzip, deflate, br"
}

Tap30Header = {
    "Host": "tap33.me",
    "Connection": "keep-alive",
    "Content-Length": "63",
    "User-Agent": "".join(random.choices(user_agents)),
    "content-type": "application/json",
    "Accept": "*/*",
    "Origin": "https://app.tapsi.cab",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://app.tapsi.cab/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"
}

DivarHeader = {
    "Host": "api.divar.ir",
    "Connection": "keep-alive",
    "Content-Length": "22",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "".join(random.choices(user_agents)),
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://divar.ir",
    "Sec-Fetch-Site": "same-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://divar.ir/my-divar/my-posts",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "fa-IR,fa;q\u003d0.9,en-GB;q\u003d0.8,en;q\u003d0.7,en-US;q\u003d0.6"
}

BamaHeader = {
    "authority": "bama.ir",
    "method": "POST",
    "user-agent": "".join(random.choices(user_agents)), 
    "path": "/signin-send-otp",
    "scheme": "https",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,fa;q=0.8",
    "content-length": "22",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "cookie": "__cf_bm=dpfdTuYlw7TCbyGWi4bqMm404f.jQgKWjKlswZRqNkE-1630749094-0-ASFpgeyWkIEaiHCNZpjFg6HvoaCKKFdse8ua169vw5K/KL+fVm9XPkSepMf6YHTLoxENZmecrF/nB6Iy7d+SjEfDPagaU8pkk+Dehh6OrEI44kOrafgPq0iDgLWduZiT2llyKryxIB94lp0JvdZsR9k+CjSOvowRAAM571uM6RgA; __cflb=02DiuFDZJj38KoK7EoAEWmzXoRsWGNYCNVpAriwD2t2s6; _ga=GA1.2.314976238.1630749108; _gid=GA1.2.1461821543.1630749108; _gat_gtag_UA_119698040_4=1; _gat_UA-119698040-4=1; CSRF-TOKEN-BAMA-COOKIE=CfDJ8J1kbi79JwRGrK8gPtbQQY76KnJGEAibnLsGWm9b6IQGXQY7Bqn6hngT1kjB9Z49KyKDM2_NyJRmO3AJVobkUBTvT7s_XQCwSHN9URwNE3-po1-sg2ormefggFAtDGEON_Hl73oyKWXFwEHnb3ILXVU",
    "csrf-token-bama-header": "CfDJ8J1kbi79JwRGrK8gPtbQQY7V0S5EeReRhhpjBoePccND89QJ7HLNBqzJkLpmmW4pgjHoLTwx9lHhC6cxHUGSDYxAQUxhYBchVaZ2LGTQmPAIsn-JFikRSyIy6MZCls3webta3kMfBvbbnGM2pj5OSTA",
    "origin": "https://bama.ir",
    "referer": "https://bama.ir/Signin?ReturnUrl=%2Fprofile",
    "sec-ch-ua": '"Google Chrome";v="93"," Not;A Brand";v="99","Chromium";v="93"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest"
}

DigiKalaHeader = {
    "Host": "api.digikala.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "X-Web-Optimize-Response": "1",
    "X-Web-Client": "desktop",
    "Content-Length": "57",
    "Origin": "https://www.digikala.com",
    "Connection": "keep-alive",
    "Referer": "https://www.digikala.com/",
    "Cookie": "tracker_glob_new=68O3R39; tracker_session=bQEHxR4; TS01e4b47a=0102310591e6514d31309b081241eb51abd1ca76f2a7f048e58f2f0b0b14dbe94b741af431c6b5faf9c1ef2eb9138be99665e63214231507450cfa92ca173360e507a9b90380d0c1d5b585f0c4f357e245eadd8edf; _sp_ses.13cb=*; _sp_id.13cb=78186e05-414b-4b29-a434-f5ae196220b0.1662461959.1.1662461974.1662461959.6ab98e45-8f5d-4c09-915f-79efd3b6f0da",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1",
    "Sec-GPC": "1",
    "TE": "trailers"
    }

AlibabaHeader = {
    "Host": "ws.alibaba.ir",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "ab-channel": "WEB-NEW,PRODUCTION,CSR,www.alibaba.ir,N,Firefox,91.0,N,N,Linux",
    "Content-Length": "28",
    "Origin": "https://www.alibaba.ir",
    "Connection": "keep-alive",
    "Referer": "https://www.alibaba.ir/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1",
    "Sec-GPC": "1"
    }

SheypoorHeader = {
    "Host": "www.sheypoor.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=utf-8",
    "Content-Length": "26",
    "Origin": "https://www.sheypoor.com",
    "Connection": "keep-alive",
    "Referer": "https://www.sheypoor.com/session",
    "Cookie": "AMP_TOKEN=%24ERROR; ts=f1b5d1185a29489786bbb32e0e4590a1; track_id=64e2daddd086c1d0d0351987c65df966; _ga=GA1.2.502817657.1662464768; _gid=GA1.2.1845818780.1662464768; _gat=1",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "TE": "trailers"
    }

KomodaHeader = {
    "Host": "api.komodaa.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "web-user-agent": "komodaa/5.8.6.236 " + "".join(random.choices(user_agents)),
    "install-ref": "WEB",
    "Content-Length": "30",
    "Origin": "https://www.komodaa.com",
    "Connection": "keep-alive",
    "Referer": "https://www.komodaa.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1",
    "Sec-GPC": "1"
}

BornosHeader = {
    "Host": "bornosmode.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-CSRF-TOKEN": "mNvstxgBZVkBJVQpq1rl36iH3AJ2h0jBRzgB18ZZ",
    "X-Requested-With": "XMLHttpRequest",
    "Content-Length": "28",
    "Origin": "https://bornosmode.com",
    "Connection": "keep-alive",
    "Referer": "https://bornosmode.com/login/?_back=https%3A%2F%2Fbornosmode.com%2F",
    "Cookie": "XSRF-TOKEN=eyJpdiI6Im80SzdBZ2N6UEZHTGcxeTVwYXN3WlE9PSIsInZhbHVlIjoiYUcvdWxkWC9zd05Fbk5sZjJEOVprS0cyYSszWVNjVEtMMlJCbGNSWjlPY08vRlF5SlZDWkZHb2hPMHlTWklucFFyK0lTL3FIWnYrb2FVSUZUK1RLSEVMWlMwL0I5VHNpOUU3ZjM2a25Ublozd05LZmFIeFRjVzRqTGZ3R0w1T1QiLCJtYWMiOiJmNGRkOTY4ZWJjM2ExZGI1NDAxY2UzZmU0MDlkZjE5NzRiYTNlNDcyMTE5MTRhYTEyYWNmZjFiZDQwMDIxYTY4IiwidGFnIjoiIn0%3D; bornosmode_session=eyJpdiI6IllIR2pzcG1NRUwvbDNOMHhTNlgvQnc9PSIsInZhbHVlIjoiUkt0MzdkcEtFbExWL25IZVZZd2xBQkJuazdwV3BGMkorbkYyQ3JxYVM4andoZERWeTBEV1c2U1FWaE1OLzduV1owN3lCVzh2bUZpQjlxWXNJb0NXRGZTZ1pqakFNZlJHUE9QaWtZNTlEYzFBeXpUSUJmTnNNUHBlaXkrWkhhdFQiLCJtYWMiOiI3OGYyN2QxNWExNTFiMjRmZDRhNjcwNjU2YzQzNTg5Y2E0OWYzMzE2ZGVmMjYxNzYyYTdiOTBjZTY3YTBmNWFhIiwidGFnIjoiIn0%3D",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "TE": "trailers"
}

BaarbaanetHeader = {
    "Host": "baarbaanet.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json;charset=utf-8",
    "CSN": "395733078",
    "CVS": "2.0.0",
    "CTY": "W",
    "Content-Length": "55",
    "Origin": "https://baarbaanet.com",
    "Connection": "keep-alive",
    "Referer": "https://baarbaanet.com/login",
    "Cookie": "wfpk=395733078",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "TE": "trailers"
}

LivitoHeader = {
    "Host": "livito.tv",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "Content-Length": "83",
    "Origin": "https://livito.tv",
    "Connection": "keep-alive",
    "Referer": "https://livito.tv/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "DNT": "1",
    "Sec-GPC": "1",
    "TE": "trailers"
}

ZarinplusHeader = {
    "Host": "api.zarinplus.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json; charset=utf-8",
    "Content-Length": "31",
    "Origin": "https://pwa.zarinplus.com",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1",
    "Sec-GPC": "1",
    "Referer": "https://pwa.zarinplus.com/",
    "Connection": "keep-alive",
    "TE": "trailers"
}

BehtarinoHeader = {
    "Host": "bck.behtarino.com",
    "User-Agent": "".join(random.choices(user_agents)),
    "Accept": "application/json",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/json",
    "User-Id": "HujvHsu79nHn3DnAXStfHnTU6dniYk",
    "Content-Length": "23",
    "Origin": "https://behtarino.com",
    "Connection": "keep-alive",
    "Referer": "https://behtarino.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "DNT": "1",
    "Sec-GPC": "1",
    "TE": "trailers"
}
