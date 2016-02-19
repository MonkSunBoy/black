from scapy.all import *

def packet_callback(packet):
	if packet[TCP].payload:
		http_packet = str(packet[TCP].payload)
		print http_packet

sniff(filter="tcp port 80", prn=packet_callback, store=0)
