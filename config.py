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

{flash}{white}███████╗██████╗  █████╗ ███╗   ███╗  {red}  ██████╗ ██╗   ██╗
{flash}{white}██╔════╝██╔══██╗██╔══██╗████╗ ████║  {red}  ██╔══██╗╚██╗ ██╔╝
{flash}{white}███████╗██████╔╝███████║██╔████╔██║  {red}  ██████╔╝ ╚████╔╝ 
{flash}{white}╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║  {red}  ██╔═══╝   ╚██╔╝  
{flash}{white}███████║██║     ██║  ██║██║ ╚═╝ ██║  {red}  ██║        ██║   
{flash}{white}╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝  {red}  ╚═╝        ╚═╝   
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
