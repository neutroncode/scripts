#!/usr/bin/env python
# Fake hacking tool for the lulz
# Nicked from a script kiddie.
import pause
from optparse import OptionParser
import sys

parser = OptionParser(usage="Delete system32 for optimal performance!")
parser.add_option("-i", "--ip", dest="ip", help="Specifies IP to be DoSed.")
(options, args) = parser.parse_args()
IP = options.ip
packets = 5

print("1337 H4X03R DoS Tool v4.20 \n")
print("Searching for open port(s)...")
pause.seconds(1)
print("Port 1080 open, selecting it...")
pause.seconds(2)
print("Simulating 1000 HTTP Clients...")
pause.seconds(0.2)
print("Starting DoS on " + str(IP) +"... \n")
pause.seconds(1)

while 1 == 1:
	try:
		print("DoSing IP: " + str(IP) + "  ---  " + str(packets) + " packets sent.")
		packets += 10
		pause.seconds(0.05)
	except KeyboardInterrupt:
		print("Stats: Sent " + str(packets) + " packets, 0 recieved, 100% loss, 0% success.")
		print("See, I told you this thing works 100% of the time!")
		print("Interrupted by user, exiting...")
		sys.exit(0)
