#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
import getopt

#parse options and arguments

opt, arg = getopt.getopt(sys.argv[1:],'h:p:',['host=','ports='])

for co,ca in opt:
    if co in ('-h','-host'):
        remoteServer = ca
    elif co in ('-p','--ports'):
        portsInput = ca


# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input

if not remoteServer: remoteServer = input("Enter a remote host to scan: ")
if not portsInput: portsInput        = input("Enter ports to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)
portsStr = list(portsInput.split(","))
ports = []
for each in portsStr:
    ports.append(int(each))

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

try:
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        else:
            print("Port {}: 	 Closed".format(port))
        sock.close()

except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

# Printing the information to screen
print(f"Scanning Completed in: {total} ")