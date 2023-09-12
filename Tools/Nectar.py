import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("NECTER")
print(ascii_banner)

print("Usage:python3 necter.py <target ip/hostname>")
#  STATING THE TARGET --> checking there are only two argument entered

if len(sys.argv) == 2:
	
	# TRANSLATING THE HOSTNAME TO IPv4
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalid amount of Argument")

# TAKING THE TARGET
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
	
	# DELECRING THE PORT RANGE
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		#Ends connection if a port does not respond in 1 second
		
        #Returns an error indicator; Open port = 0 Closed port =1
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program !!!!")
		sys.exit()
except socket.gaierror:
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()
except socket.error:
		print("\ Server not responding !!!!")
		sys.exit()

