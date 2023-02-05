import re
import sys
import platform
import subprocess
import os
from os import environ

SUPPORTED_PLATFORMS = ['Windows']

PLATFORM_IS_SUPPORTED = False

PROCESS_IS_RUNNING = True

OUTPUT_FILE_NAME = "out"

OUTPUT_FILE_LOCATION = 'C://Users//'+os.getenv('username')+'//Downloads'

help_exec = False

def exit_r(reason: str):
    PROCESS_IS_RUNNING = False
    print('Terminating process. ' + reason)
    sys.exit()

def check_platform_support():#this function checks if this program is compatible with the platform or not
    global SUPPORTED_PLATFORMS , PLATFORM_IS_SUPPORTED
    for p in SUPPORTED_PLATFORMS:
        if p == platform.system() and 'ANDROID_ROOT' not in environ:
            PLATFORM_IS_SUPPORTED = True
            return
    if platform.system() == 'Linux':
        exit_r('\n[-] \'' + 'Linux Android' + '\' platform is not supported(Root instead). \nCurrently supported platforms are: \n' + str(SUPPORTED_PLATFORMS))
    else:
        exit_r('\n[-] \'' + platform.system() + '\' platform is not supported. \nCurrently supported platforms are: \n' + str(SUPPORTED_PLATFORMS))
        

def get_ipconfig()->str:
    
    if platform.system() == 'Windows':
        ip_config = subprocess.run('ipconfig' , capture_output=True , text=True)
        return ip_config.stdout
    
    elif platform.system() == 'Linux':
        pass
    
def get_user_profiles()->str:
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
        pass

def get_keys(profiles: str):#get the password and related details
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
        pass

def save_all_data(output_file_name: str,output_file_location: str):#saves the data in a file
    try:
        if platform.system() == "Windows":
            out = open(output_file_location+'//'+output_file_name+".txt" , 'w')
        
        elif platform.system() == "Linux":
            pass
    except:
        exit_r('[-] Please specify correct output location and name.')

    print('[+] Getting IP configuration.')
    out.writelines(get_ipconfig())
    print('[+] Getting user profiles.')
    out.writelines(get_user_profiles())
    up = get_user_profiles()
    print('[+] Getting keys.')
    out.writelines(get_keys(up))
    print('[+] Output file saved. '+output_file_location+'//'+output_file_name+".txt")
    out.close()

def help():
    print("\n@author: Raghav Gohil")
    print("\nAbout:\nThis package is made to acquire all the forgotten wifi passwords and related data and store it in your desired place.\nYou can even store it in your pendrive.\nUsually, if the location and name of the file is not specifed, the output file containing the data will be stored in the downloads folder with the name \'out.txt\'.\nYou can go full-on hacker mode and clone the data from a target-pc in mere seconds.")
    print("\nOptions:\n-h : help (cannot be used with multiple options).\n-o<whitespace><name>: specify output file name.\n-ol<whitespace><location>: specify output location.")
    print('\n')

def arg_exec():#execute the given arguments
    global OUTPUT_FILE_LOCATION,OUTPUT_FILE_NAME,help_exec
    for arg in enumerate(sys.argv):
        if(arg[1] == '-h'):
            help_exec = True
        if(arg[1] == '-o' and (len(sys.argv)-1) > arg[0]):
            if(str(sys.argv[(arg[0]+1)])[0] != '-'):
                OUTPUT_FILE_NAME = sys.argv[(arg[0]+1)]
            else:
                exit_r("[-] Match option syntax. Use gwfp -h for help.")
        if(arg[1] == '-ol' and (len(sys.argv)-1) > arg[0]):
            if(str(sys.argv[(arg[0]+1)])[0] != '-'):
                OUTPUT_FILE_LOCATION = sys.argv[(arg[0]+1)]
            else:
                exit_r("[-] Match option syntax. Use gwfp -h for help.")

def main():
    global OUTPUT_FILE_LOCATION,OUTPUT_FILE_NAME,help_exec
    check_platform_support()
    arg_exec()
    if(('-h' in sys.argv) and len(sys.argv)>2):
        exit_r("[-] Match option syntax. Use gwfp -h for help.")
    elif(PLATFORM_IS_SUPPORTED and ('-h' not in sys.argv)):
        save_all_data(OUTPUT_FILE_NAME,OUTPUT_FILE_LOCATION)
        exit_r('\n[+] Process ended.')
    elif(PLATFORM_IS_SUPPORTED and ('-h' in sys.argv)):
        if help_exec:
            help()