#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from pox.lib.addresses import *

print "IP"
ip = IPAddr("192.168.1.1")
print str(ip)
print ip.toUnsignedN()
print ip.toRaw()
ip = IPAddr(16885952,networkOrder=True)
print str(ip)

#####

print "MAC"
mac = EthAddr("00:00:10:10:20:10")
print str(mac)

if mac.is_multicast == True: 
	print "Multicast"
else:
	print "Nao multicast"

print mac.toRaw()
print mac.toStr()