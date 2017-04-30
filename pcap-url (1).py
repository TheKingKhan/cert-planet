#!/usr/bin/env python

import dpkt
import sys

f = open(sys.argv[1], "r")
pcap = dpkt.pcap.Reader(f)

http_ports = [80, 8080] # Add other ports if you website on non-standard port.
urls = [ ]

for timestamp, buf in pcap:
    eth = dpkt.ethernet.Ethernet(buf)
    ip = eth.data
    tcp = ip.data
    if tcp.__class__.__name__ == 'TCP':
        if tcp.dport in http_ports and len(tcp.data) > 0:
            try:
                http = dpkt.http.Request(tcp.data)
                urls.append(http.headers['host'] + http.uri)
            except Exception as e:
                # Just in case we come across some stubborn kid.
                print "[-] Some error occured. - %s" % str(e)
f.close()

print "[+] URLs extracted from PCAP file are:\n"
for url in urls:
    print url
