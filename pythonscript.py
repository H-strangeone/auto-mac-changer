import subprocess
import optparse

parser=optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="its MAC address")

(options, arguments)=parser.parse_args()

interface=options.interface
new_mac=options.new_mac

subprocess.call(["sudo ifconfig"])
subprocess.call(["sudo ifconfig", interface ,"down"])
subprocess.call(["sudo ifconfig", interface,"hw ether", new_mac])
subprocess.call(["sudo ifconfig", interface, "up"])
subprocess.call(["sudo ifconfig"])