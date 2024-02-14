import subprocess
import optparse

parser=optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="its MAC address")

(options, arguments)=parser.parse_args()

def change_mac(interface, new_mac):
    subprocess.call(["sudo ifconfig "+interface+" down"], shell= True)#do not use , cause fir wo list ke elements samjhega har ek cheez ko unko concat karne ki jagah you can either use --thing or -thing both will work fine like --interface -i
    subprocess.call(["sudo ifconfig "+interface+" hw "+"ether "+new_mac], shell=True)
    subprocess.call(["sudo ifconfig "+interface+" up"],shell=True)

change_mac(options.interface ,options.new_mac)