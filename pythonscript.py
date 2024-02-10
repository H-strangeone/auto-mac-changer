import subprocess
import optparse
parser=optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change its MAC address")
parser.parse_args
interface=input("interface  =")
new_mac=input("mac  address =")
subprocess.call("ifconfig", shell=True)
subprocess.call("sudo ifconfig", interface ,"down", shell=True)
subprocess.call("sudo ifconfig", interface,"hw ether", new_mac, shell= True)
subprocess.call("sudo ifconfig", interface, "up",  shell=True)