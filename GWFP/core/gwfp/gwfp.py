import re
import sys
import platform
import subprocess
import os
from os import environ

SUPPORTED_PLATFORMS = ['Windows' , 'Linux']

PLATFORM_IS_SUPPORTED = False

PROCESS_IS_RUNNING = True

def exit_r(reason: str):
    PROCESS_IS_RUNNING = False
    print('Terminating process. ' + reason)
    sys.exit()

def check_platform_support():
    global SUPPORTED_PLATFORMS , PLATFORM_IS_SUPPORTED
    for p in SUPPORTED_PLATFORMS:
        if p == platform.system() and 'ANDROID_ROOT' not in environ:
            PLATFORM_IS_SUPPORTED = True
            return
    if platform.system() == 'Linux':
        exit_r('\n[-] \'' + 'Linux Android' + '\' platform is not supported(Root instead). \nCurrently supported platforms are: \n' + str(SUPPORTED_PLATFORMS))
    else:
        exit_r('\n[-] \'' + platform.system() + '\' platform is not supported. \nCurrently supported platforms are: \n' + str(SUPPORTED_PLATFORMS))
        

def get_ipconfig():
    
    if platform.system() == 'Windows':
        ip_config = subprocess.run('ipconfig' , capture_output=True , text=True)
        return ip_config.stdout
    
    elif platform.system() == 'Linux':
        if_config = subprocess.run('ifconfig' , capture_output=True , text=True)

        return if_config.stdout
    
def get_user_profiles():
    if platform.system() == 'Windows':
        try:
            w_user_profiles = subprocess.run('netsh wlan show profiles' , capture_output=True , text=True)
            superset = re.split( r'\s' , w_user_profiles.stdout)
            pointer = 0
            w_user_profiles = []
            while pointer < len(superset):
                if superset[pointer-6] == 'Profile': w_user_profiles.append(superset[pointer])
                pointer += 1
            return w_user_profiles
        except:
            exit_r('[-] Failed to get user profiles')
    
    elif platform.system() == 'Linux':
        try:
            l_user_profiles = subprocess.run('cd /etc/NetworkManager/system-connections/*' , capture_output=True , text=True)
            return l_user_profiles
            
        except:
            exit_r('[-] Failed to get user profiles')

def get_keys(profiles):
    if platform.system() == 'Windows':
        try:
            keys = []
            for x in profiles:
                search = subprocess.run('netsh wlan show profiles '+x+' key=clear' , capture_output=True , text=True)
                keys.append(search.stdout)
            return keys
        except:
            exit_r('[-] Failed to get keys')
        
    elif platform.system() == 'Linux':
        try:
            a = 0/0
        except:
            exit_r('[-] Failed to get keys')

def save_all_data():
    try:
        if platform.system() == "Windows":
            out = open('C://Users//'+os.getenv('username')+'//Downloads/out.txt' , 'w')
        
        elif platform.system() == "Linux":
            out = open(f'/home/{os.getlogin()}/Downloads/out.txt' , 'w')
    except:
        print('[-] Unable to find downloads folder.')
    print('[+] Getting IP configuration.')
    out.writelines(get_ipconfig())
    print('[+] Getting user profiles.')
    out.writelines(get_user_profiles())
    up = get_user_profiles()
    print('[+] Getting keys.')
    out.writelines(get_keys(up))
    print('[+] Output file saved.')
    out.close()

def main():
    check_platform_support()
    if PLATFORM_IS_SUPPORTED:
        save_all_data()
        exit_r('\n[+] Process ended.')