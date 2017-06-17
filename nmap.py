#!/usr/bin/env python
#encoding:utf-8
import pause

title = "Starting Nmap 7.25BETA2 ( https://nmap.org ) at 2016-09-21 08:55 NZST"

reportHdr = "Nmap scan report for "

info = '''
Host is up (0.00011s latency).
Not shown: 910 closed ports
'''
table = "PORT     STATE SERVICE"
row0 = "53/tcp   open  dns"
row1 = "80/tcp   open  apache2"
row2 = "443/tcp  open  https"
row3 = "1080/tcp open  socks5"
row4 = "4444/udp open  skype/VoIP"

end = "Nmap done: 1 IP address (1 host up) scanned in 30.5 seconds"

while 1 == 1:
	print title
	pause.seconds(0.1)
	print reportHdr
	pause.seconds(0.1)
	print info
	pause.seconds(0.1)
	print table
	pause.seconds(0.1)
	print row0
	pause.seconds(0.1)
	print row1
	pause.seconds(0.1)
	print row2
	pause.seconds(0.1)
	print row3
	pause.seconds(0.1)
	print row4
	pause.seconds(0.1)
	print end + "\n"
	pause.seconds(0.1)
