#/usr/bin/env python3

# importing modules
import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

# init Name Server class
NS = dr.Resolver()

# Target
Domain = 'inlanefreight.com' # replace with your own target

# Set Name Servers
NS.nameservers = ['ns1.inlanefreight.com', 'ns2.inlanefreight.com'] # replace with your own target's nameservers

# List of found subdomains
Subdomains = []

def AXFR(domain, nameserver):
	# try zone transfers with target's domain and nameserver
	try:
		axfr = dz.from_xfr(dq.xfr(nameserver, domain)) # Perform the zone transfer
		
		if axfr: # if the zone transfer is successful
			print("[*] Successful Zone Transfer from {}".format(nameserver))
		
			# add found subdomains to global "Subdomain" list
			for record in axfr:
				Subdomains.append("{}.{}".format(record.to_text(), domain))
		
	# failure of zone transfer
	except Exception as error:
		print(error)
		pass

if __name__ == "__main__":
	pass	
