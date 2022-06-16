#/usr/bin/env python3

# importing modules
import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

# init Name Server class
NS = dr.Resolver()

# Target
Domain = "inlanefreight.com" # replace with your own target

# Set Name Servers
NS.nameservers = ["ns1.inlanefreight.com", "ns2.inlanefreight.com"]

# List of found subdomains
Subdomains = []
