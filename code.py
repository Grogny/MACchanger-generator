import subprocess
import optparse

print("    __  ___  ___     ______          __")
print("   /  |/  / /   |   / ____/  _____  / /_   ____ _   ____    ____ _  ___    _____")
print("  / /|_/ / / /| |  / /      / ___/ / __ \ / __ `/  / __ \  / __ `/ / _ \  / ___/")
print(" / /  / / / ___ | / /___   / /__  / / / // /_/ /  / / / / / /_/ / /  __/ / /")
print("/_/  /_/ /_/  |_| \____/   \___/ /_/ /_/ \__,_/  /_/ /_/  \__, /  \___/ /_/")
print("                                                         /____/")

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface can be ether0 or wlan0")
    parser.add_option("-m", "--macaddress", dest="mac_address", help="Your new MAC address")
    (options, arguments) = parser.parse_args() # options = ether0 ou wlan0 + MAC et arguments = -command

    if not options.interface:
        parser.error("[!] Next time, specify your interface, --help for more information")
    elif not options.mac_address:
        parser.error("[!] Next time, specify your MAC address, --help for more information")
    return options

def change_mac(interface, mac_address):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])
    subprocess.call(["ifconfig", interface])

    print("[+] Your new " + interface + " MAC address is now: " + mac_address + " !")

options = get_arguments()
# change_mac(options.interface, options.mac_address)

ifconfig = subprocess.check_output(["ifconfig", options.interface])
