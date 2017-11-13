import os
import sys
import socket

def baseScan(string, number):
    for i in range(1,number):
        try:
            s = socket.socket()
            s.connect((string, i))
            s.send("Test")
            banner = s.recv(1024)
            if banner:
                print("Port " + str(i) + " open:" + banner)
        except:
            print("Port " + str(i) + " closed")
    
def ipCorrection(string):
    parsed = string.split(".")
    for x in parsed:
        if not (x.isdigit()):
            return False;
        elif(len(str(x))>3):
            return False;
    return True;

def switchAddition(ipaddr, length):
    if(length==2):
        baseScan(ipaddr, 1024)
    elif(length==3):
        if(sys.argv[2].lower() == "--all"):
            baseScan(ipaddr, 65535)
    else:
        print("Incorrect switches. Type --help for more information")
    
            
        
if not ipCorrection(sys.argv[1]) and not (sys.argv[1].lower() == "--help"):
    print("Incorrect IP Address. Type --help for more information")
    exit()
elif(sys.argv[1].lower() == "--help"):
    print("Portscanner.py [ip address] [-all|optional]")
else:
    switchAddition(sys.argv[1], len(sys.argv)) 
