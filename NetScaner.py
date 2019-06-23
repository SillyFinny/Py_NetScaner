#!/usr/bin/env python

import scapy.all as scapy
import argparse

def take_input():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Enter target IP. for example: '192.192.192.192/24'")
	options = parser.parse_args()
	return options

def scan(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arpbrodcast = broadcast/arp_request
	answered_list = scapy.srp(arpbrodcast, timeout=1, verbose=False)[0]
	
	client_list = []
	
	for element in answered_list:
		client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
		client_list.append(client_dict)
	return(client_list)

def print_res(result_list):
	print("IP\t\t\tMAC Address\n------------------------------------")
	for client in result_list:
		print(client["IP"] + "\t\t" + client["MAC"])

options = take_input()
scan_result = scan(options.target)
print_res(scan_result)