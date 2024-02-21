import subprocess
import optparse
import time
import random

def get_args():
    parser=optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    # parser.add_option("-m", "--mac", dest="new_mac", help="its MAC address")
    parser.add_option("-b", "--bool", dest="bool", help="boolean value either true or false")
    (options, arguments)=parser.parse_args()
    if not options.interface:
        print("use --help and input a real interface")
    # elif not options.new_mac:
    #     print("use --help and input a real mac address")
    else:
        return options

def change_mac(interface,bool):
    subprocess.call(["sudo ifconfig "+interface+" down"], shell= True)#don not use , cause fir wo list ke lements samjhega har ek cheez ko unko concat karne ki jagah you can either use --thing or -thing both will work fine like --interface -i
    subprocess.call(["sudo ifconfig "+interface+" hw "+"ether "+str(12)+":"+str(random.randint(11,99))+":"+str(random.randint(11,99))+":"+str(random.randint(11,99))+":"+str(random.randint(11,99))+":"+str(random.randint(11,99))], shell=True)
    subprocess.call(["sudo ifconfig "+interface+" up"],shell=True)
    
options=get_args()
while(bool==True):
    change_mac(options.interface, options.bool)
    time.sleep(10)