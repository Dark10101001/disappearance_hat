import random
import subprocess as su
from time import sleep
import os
def adders():
    blue='\033[34m'
    banner=blue+""" 
    
    _ _                                                           
  __| (_)___  __ _ _ __  _ __   ___  __ _ _ __ __ _ _ __   ___ ___ 
 / _` | / __|/ _` | '_ \| '_ \ / _ \/ _` | '__/ _` | '_ \ / __/ _ '
| (_| | \__ \ (_| | |_) | |_) |  __/ (_| | | | (_| | | | | (_|  __/
 \__,_|_|___/\__,_| .__/| .__/ \___|\__,_|_|  \__,_|_| |_|\___\___|
                  |_|   |_|                                        
 _           _   
| |__   __ _| |_ 
| '_ \ / _` | __|
| | | | (_| | |_             
|_| |_|\__,_|\__|            

                        _________________________________
                        (________________________________)   
         \033[32m               |                                |
                        |                                |
                        |                                |     
                        /_________________________________\    
                       (___________________________________)


                                1-
                                this tool changes the MAC address
                                of the device so that it helps you
                                to connect to the internet securely
                                and one of the advantages of this tool
                                is that it changes the IP address as 
                                many times as you want and this tool
                                is still under development
    
                                2-
                                how do you work it out

                                1- choose the number of times you want the 
                                tool to run, knowing that it changes the IP
                                every 3 seconds
                                2- choose the type you want to change
                                 MAC adderss from (wlan0) or (lo) or (eth0)

tool maker: Dark

    \033[31m
                                            important Alert:
                                            it may work on linux and termux 
                                            only or linux only
    """
    print(banner)

    what=int(input("how many: "))

    l=["00:11:22:33:44:63","00:11:22:33:44:55","00:11:22:33:44:33","00:11:22:33:44:55",
    "00:11:22:33:44:66","00:11:22:33:44:63","00:11:22:33:44:61","00:11:22:33:44:60",
    "00:11:22:33:44:67"]
    maca=input("what: ")
    

    def mac():
        
            for x in range(what):

                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[0],shell=True)
                sleep(3)
                print("\033[33m[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)
            
                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[1],shell=True)
                sleep(3)

                print("\033[33m[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)

                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[2],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)

                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[3],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)
        ########
                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[4],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)
            
            
                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[5],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)

                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[6],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)


                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[7],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)
            
                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[8],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
                sleep(2)
            
                go=su.call("ifconfig "+maca+" down",shell= True)
                go=su.call("ifconfig "+maca+" hw ether "+l[3],shell=True)
                sleep(3)
                print("[+] the MAC address has changed [+]")
                go=su.call("ifconfig "+maca+" up",shell=True)  
            
            print("Been completed :) <'jast'>!")
        
    
    mac()
adders()
