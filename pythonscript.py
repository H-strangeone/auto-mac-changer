import subprocess

subprocess.call("ifconfig", shell=True)
subprocess.call("sudo ifconfig wlp0s20f3 down", shell=True)
subprocess.call("sudo ifconfig wlp0s20f3 hw ether 00:11:22:33:44:55", shell= True)
subprocess.call("sudo ifconfig wlp0s20f3 up",  shell=True)