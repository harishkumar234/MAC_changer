import subprocess
import optparse

def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()

(options, _) = get_arguments()
interface = options.interface
new_mac = options.new_mac

if not interface:
    print("Please specify an interface. Use -i or --interface.")
elif not new_mac:
    print("Please specify a new MAC address. Use -m or --mac.")
else:
    change_mac(interface, new_mac)
