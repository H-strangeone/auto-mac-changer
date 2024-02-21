import subprocess
import optparse

def get_args():
    parser=optparse.OptionParser()

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="its MAC address")

    (options, arguments)=parser.parse_args()
    if not options.interface:
        print("use --help and input a real interface")
    elif not options.new_mac:
        print("use --help and input a real mac address")
    else:
        return options

def change_mac(interface, new_mac):
    subprocess.call(["sudo ifconfig "+interface+" down"], shell= True)#do not use , cause fir wo list ke elements samjhega har ek cheez ko unko concat karne ki jagah you can either use --thing or -thing both will work fine like --interface -i
    subprocess.call(["sudo ifconfig "+interface+" hw "+"ether "+new_mac], shell=True)
    subprocess.call(["sudo ifconfig "+interface+" up"],shell=True)
options=get_args() 
change_mac(options.interface ,options.new_mac)
ifconfig_result=subprocess.check_output(["ifcon"])