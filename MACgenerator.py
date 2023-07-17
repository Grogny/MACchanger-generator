from randmac import RandMac
from colorama import Fore

import colorama 

colorama.init()
print(f"""
 {Fore.BLUE}__  __          _____ {Fore.YELLOW}                               _             
{Fore.BLUE}|  \/  |   /\   / ____|{Fore.YELLOW}                              | |            
{Fore.BLUE}| \  / |  /  \ | |     {Fore.YELLOW}__ _  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
{Fore.BLUE}| |\/| | / /\ \| |    {Fore.YELLOW}/ _` |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
{Fore.BLUE}| |  | |/ ____ \ |___{Fore.YELLOW}| (_| |  __/ | | |  __/ | | (_| | || (_) | |   
{Fore.BLUE}|_|  |_/_/    \_\_____{Fore.YELLOW}\__, |\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                 {Fore.YELLOW} __/ |                                        
                                 {Fore.YELLOW}|___/                                                                                
    """)
while True:
    nb = input(f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}How many address? ({Fore.RED}max. 9{Fore.WHITE}): ")
    if not nb.isnumeric():
        print(f"{Fore.LIGHTGREEN_EX}[!] {Fore.WHITE}Please enter a {Fore.RED}number")
    elif int(nb) > 9:
        print(f"{Fore.LIGHTGREEN_EX}[!] Max. 9, {Fore.WHITE}please enter a {Fore.RED}valid ammount of address")
    else:
        for i in range(0, int(nb)):
            print(f"[{i+1}]", RandMac("00:00:00:00:00:00"))
        break
