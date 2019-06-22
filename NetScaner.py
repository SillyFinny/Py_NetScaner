#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpbrodcast = broadcast/arp_request

scan("enter IP") # example 192.192.192.192/24
