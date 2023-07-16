from colorama import Fore

import subprocess
import colorama
import optparse

def change_mac(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])
    print(f"{Fore.LIGHTGREEN_EX}[+] {Fore.WHITE}Your new {Fore.RED}{interface} {Fore.WHITE}is now {Fore.RED}{mac_address} {Fore.WHITE}!")

    ifconfig = subprocess.check_output(["ifconfig", interface])
    print(f"\n {Fore.WHITE}{ifconfig}")

def main():
    colorama.init()
    print(f"""
{Fore.BLUE}    __  ___  ___     ______  {Fore.YELLOW}        __
{Fore.BLUE}   /  |/  / /   |   / ____/  {Fore.YELLOW}_____  / /_   ____ _   ____    ____ _  ___    _____{Fore.WHITE}
{Fore.BLUE}  / /|_/ / / /| |  / /      {Fore.YELLOW}/ ___/ / __ \ / __ `/  / __ \  / __ `/ / _ \  / ___/{Fore.WHITE}
{Fore.BLUE} / /  / / / ___ | / /___   {Fore.YELLOW}/ /__  / / / // /_/ /  / / / / / /_/ / /  __/ / /{Fore.WHITE}
{Fore.BLUE}/_/  /_/ /_/  |_| \____/   {Fore.YELLOW}\___/ /_/ /_/ \__,_/  /_/ /_/  \__, /  \___/ /_/{Fore.WHITE}
{Fore.BLUE}                                                         {Fore.YELLOW}/____/{Fore.WHITE}
""")
    
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface can be ether0 or wlan0")
    parser.add_option("-m", "--macaddress", dest="mac_address", help="Your new MAC address")
    (options, arguments) = parser.parse_args() 

    if not options.interface:
        parser.error(f"{Fore.LIGHTGREEN_EX}[!] {Fore.WHITE}Next time, specify your {Fore.RED}interface{Fore.WHITE}, --help for more information")
    elif not options.mac_address:
        parser.error(f"{Fore.LIGHTGREEN_EX}[!] {Fore.WHITE}Next time, specify your {Fore.RED}MAC address{Fore.WHITE}, --help for more information")
    else:
        change_mac(options.interface, options.mac_address)

if __name__ == "__main__":
    main()
