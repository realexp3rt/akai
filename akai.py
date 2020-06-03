#!/usr/bin/python3
import os
import json
from requests import get,session
from sys import exit
from time import sleep

import uuid

try:
    from colorizor import *

except ImportError as ier:
    print(ier)

os.system('clear')

def show_options():
    print(COLOR.BRIGHT_BLUE + '[1] ' + COLOR.WHITE + 'hide my ip once')
    print(COLOR.BRIGHT_BLUE + '[2] ' + COLOR.WHITE + 'hide my ip repeatedly')
    print(COLOR.BRIGHT_BLUE + '[3] ' + COLOR.WHITE + 'change ip')
    print(COLOR.BRIGHT_BLUE + '[4] ' + COLOR.WHITE + 'change my mac address')
    print(COLOR.BRIGHT_BLUE + '[5] ' + COLOR.WHITE + 'do it all')
    print(COLOR.BRIGHT_BLUE + '[6] ' + COLOR.WHITE + 'show ip')
    print(COLOR.BRIGHT_BLUE + '[7] ' + COLOR.WHITE + 'stop')
    print(COLOR.BRIGHT_BLUE + '[8] ' + COLOR.WHITE + 'clear')
    print(COLOR.BRIGHT_BLUE + '[9] ' + COLOR.WHITE + 'exit/quit\n')

def banner():
    print(COLOR.RED + """
          _____                    _____                    _____                    _____          
         /\    \                  /\    \                  /\    \                  /\    \         
        /::\    \                /::\____\                /::\    \                /::\    \        
       /::::\    \              /:::/    /               /::::\    \               \:::\    \       
      /::::::\    \            /:::/    /               /::::::\    \               \:::\    \      
     /:::/\:::\    \          /:::/    /               /:::/\:::\    \               \:::\    \     
    /:::/__\:::\    \        /:::/____/               /:::/__\:::\    \               \:::\    \    
   /::::\   \:::\    \      /::::\    \              /::::\   \:::\    \              /::::\    \   
  /::::::\   \:::\    \    /::::::\____\________    /::::::\   \:::\    \    ____    /::::::\    \  
 /:::/\:::\   \:::\    \  /:::/\:::::::::::\    \  /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \ 
/:::/  \:::\   \:::\____\/:::/  |:::::::::::\____\/:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\ 
\::/    \:::\  /:::/    /\::/   |::|~~~|~~~~~     \::/    \:::\  /:::/    /\:::\  /:::/    \::/    /
 \/____/ \:::\/:::/    /  \/____|::|   |           \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/ 
          \::::::/    /         |::|   |                    \::::::/    /    \::::::/    /          
           \::::/    /          |::|   |                     \::::/    /      \::::/____/           
           /:::/    /           |::|   |  author : exp3rt    /:::/    /        \:::\    \           
          /:::/    /            |::|   |                    /:::/    /          \:::\    \          
         /:::/    /             |::|   |                   /:::/    /            \:::\    \         
        /:::/    /              \::|   |                  /:::/    /              \:::\____\        
        \::/    /                \:|   |                  \::/    /                \::/    /        
         \/____/                  \|___|                   \/____/                  \/____/          
                                                                                                    
""")

banner()
show_options()

def get_mac():

  try:
    mac = open('/sys/class/net/'+"eth0"+'/address').readline()
    print (COLOR.BRIGHT_BLUE + "[#] Your New MACADDRESS is : ", mac + COLOR.WHITE)
  except:
    mac = "00:00:00:00:00:00"

def show_ip():

    getr = get('https://api.ip.sb/geoip')
    getj = getr.json()

    print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY +'IP      : ' + COLOR.RED + getj['ip'])
    print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY +'COUNTRY : ' + COLOR.RED + getj['country'])

    if 'city' in getj:
        print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY +'CITY    : ' + COLOR.RED + getj['city'])
    else:
        print(COLOR.LIGHT_CYAN + '[#] ' + COLOR.LIGHT_GRAY + 'CITY    : ' + COLOR.WHITE + 'UNKNOWN')

def start_anonsurf():
    print(COLOR.LIGHT_GREEN + '\n[*] ' + COLOR.WHITE + 'Changing IP Address ..')
    os.system('anonsurf start >/dev/null 2>&1')
    print(COLOR.LIGHT_GREEN + '[+] Changed Successfully!\n'+ COLOR.WHITE)

def change_ip_repeatedly():

    try:

        ip_change_delay = int(input(COLOR.YELLOW + '\n[?] ' + COLOR.WHITE + 'Change my IP Every '+COLOR.LIGHT_RED + '[SECONDS]' + COLOR.WHITE + ' : '))
        if(ip_change_delay == 0):

            print(COLOR.RED + '[-] Please Enter a Correct Number!' + COLOR.WHITE)
            sleep(2)
            os.system('clear')
            banner()
            show_options()
            Engine()

        print(COLOR.LIGHT_GREEN + '[*] ' + COLOR.WHITE + 'Running IP Changer Service..')
        os.system('anonsurf start >/dev/null 2>&1')
        print(COLOR.LIGHT_GREEN + '[+] Successfully Run!')
        print(COLOR.LIGHT_CYAN + '\n[*] ' + COLOR.WHITE + 'Changing IP Every' + COLOR.LIGHT_RED + ' {}S '.format(ip_change_delay) + '\n')
        print(COLOR.DARK_GRAY + '- - - - - - - - - - - - - - - - - -')

        test = ip_change_delay

        try:

            while (0<test):

                if(test >= 2):
                    sleep(ip_change_delay - 1)
                    os.system('anonsurf change ip >/dev/null 2>&1')
                elif(test >= 3):
                    sleep(ip_change_delay - 2)
                    os.system('anonsurf change ip >/dev/null 2>&1')
                elif(test >= 4):
                    sleep(ip_change_delay - 3)
                    os.system('anonsurf change ip >/dev/null 2>&1')
                elif(test >= 5):
                    sleep(ip_change_delay - 4)
                    os.system('anonsurf change ip >/dev/null 2>&1')
                elif(test == 1):
                    os.system('anonsurf change ip >/dev/null 2>&1')

                show_ip()
                print(COLOR.DARK_GRAY + '- - - - - - - - - - - - - - - - - -')

        except KeyboardInterrupt:

            os.system('clear')
            banner()
            show_options()
            Engine()

    except ValueError:
        print(COLOR.RED + '[-] Please Enter a Correct Number!' + COLOR.WHITE)
        sleep(2)
        os.system('clear')
        banner()
        show_options()
        Engine()

def stop():
    os.system('anonsurf stop >/dev/null 2>&1')
    print(COLOR.LIGHT_GREEN + '\n[+] Successfully Stopped!\n'+ COLOR.WHITE)

def change_macaddress():
    print(COLOR.LIGHT_GREEN + '\n[*] ' + COLOR.WHITE + 'Running MACCHANGER Service..')
    eth = os.listdir('/sys/class/net/')
    if 'eth0' in eth:
        os.system('macchanger eth0 -r >/dev/null 2>&1')
    elif 'wlan0' in eth:
        os.system('macchanger wlan0 -r >/dev/null 2>&1')
    else:
        print(COLOR.RED + '[-] Could not Grab the Network Interface \n'+ COLOR.WHITE)
        interface = input(COLOR.LIGHT_CYAN + '[?] Please Enter Your Network Interface Name : \n')
        os.system('macchanger {} -r >/dev/null 2>&1'.format(interface))

    print(COLOR.LIGHT_GREEN + '[+] Mac Address Changed Successfully!\n'+ COLOR.WHITE)

def goodbye():
    print(COLOR.VIOLET + '\n[-] Thanks For Using Akai!\n')
    exit()

def clear():
    os.system('clear')
    banner()
    show_options()

def Engine():

    try:

        while True:

            choice = input(COLOR.GREEN + STYLE.ITALIC + '[akai]' + COLOR.WHITE +  ' > ' + COLOR.WHITE)

            if(choice == '1' or choice.lower() == 'hide my ip once'):
                start_anonsurf()

            elif(choice == '2' or choice.lower() == 'hide my ip repeatedly'):
                change_ip_repeatedly()
                if(KeyboardInterrupt):
                    goodbye()

            elif(choice == '3' or choice.lower() == 'change ip'):

                os.system('anonsurf start >/dev/null 2>&1')
                os.system('anonsurf change ip >/dev/null 2>&1')
                print(COLOR.LIGHT_GREEN + '\n[+] Successfully Changed!\n'+ COLOR.WHITE)
                show_ip()
                print('\n')
            elif(choice == '4' or choice.lower() == 'change my mac address'):
                change_macaddress()
                get_mac()

            elif(choice == '5' or choice.lower() == 'do it all'):
                start_anonsurf()
                os.system('anonsurf change ip >/dev/null 2>&1')
                change_macaddress()
                get_mac()
            elif(choice == '6' or choice.lower() == 'show ip'):
                print('\n')
                show_ip()
                print('\n')

            elif(choice == '7' or choice.lower() == 'stop'):
                stop()

            elif(choice == '8' or choice.lower() == 'clear'):
                clear()

            elif(choice == '9'or choice.lower() == 'quit' or choice.lower() == 'exit'):
                goodbye()

            else:
                print(COLOR.RED + '[-] Wrong Command!' + COLOR.WHITE)

    except KeyboardInterrupt:
        print('\n')
        goodbye()

Engine()

