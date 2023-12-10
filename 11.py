#!/usr/bin/env python
# -*- coding: utf-8 -*-

# _________________________________________________________
# Programming : Tech Coder
# Github : https://github.com/Pypis
# Telegram: https://t.me/Pypls
# _________________________________________________________

import os, sys, time
from time import sleep

os.system("pip install rich")
time.sleep(1)
os.system("clear")

import rich
from rich.markdown import *
from rich.console import *

try:
    import requests
except ImportError:
    pypls = "# • The library will be installed (requests) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install requests")
    time.sleep(1)
    os.system("clear")

try:
    from bs4 import *
except ImportError:
    pypls = "# • The library will be installed (bs4) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install bs4")
    time.sleep(1)
    os.system("clear")

try:
    import webbrowser
except ImportError:
    pypls = "# • The library will be installed (webbrowser) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install webbrowser")
    time.sleep(1)
    os.system("clear")

try:
    import concurrent.futures
except ImportError:
    pypls = "# • The library will be installed (futures) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install futures")
    time.sleep(1)
    os.system("clear")

try:
    import mechanize
except ImportError:
    pypls = "# • The library will be installed (mechanize) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install mechanize")
    time.sleep(1)
    os.system("clear")

try:
    import stdiomask
except ImportError:
    pypls = "# • The library will be installed (stdiomask) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install stdiomask")
    time.sleep(1)
    os.system("clear")

try:
    from user_agent import *
except ImportError:
    pypls = "# • The library will be installed (user_agent) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install user_agent")
    time.sleep(1)
    os.system("clear")

try:
    from faker import *
except ImportError:
    pypls = "# • The library will be installed (faker) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install faker")
    time.sleep(1)
    os.system("clear")

try:
    import telebot
except ImportError:
    pypls = "# • The library will be installed (telebot) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install Pytelegrambotapi==4")
    time.sleep(1)
    os.system("clear")

try:
    from colorama import *
except ImportError:
    pypls = "# • The library will be installed (colorama) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install colorama")
    time.sleep(1)
    os.system("clear")

try:
    import pyfiglet
except ImportError:
    pypls = "# • The library will be installed (pyfiglet) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install pyfiglet")
    time.sleep(1)
    os.system("clear")

try:
    import names
except ImportError:
    pypls = "# • The library will be installed (names) •"
    tech = rich.markdown.Markdown(pypls, style="green")
    rich.console.Console().print(tech)
    print("")
    os.system("pip install names")
    time.sleep(1)
    os.system("clear")


webbrowser.open("https://t.me/Pypls")
time.sleep(1)
pypls = "# • Follow us on telegram ( @Pypls ) •"
tech = rich.markdown.Markdown(pypls, style="green")
rich.console.Console().print(tech)
print("\033[2;32m")
print(pyfiglet.figlet_format(" Thanks "))
time.sleep(1)
