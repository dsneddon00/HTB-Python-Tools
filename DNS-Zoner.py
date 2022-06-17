#/usr/bin/env python3

# importing modules
import dns.zone as dz
import dns.query as dq
import dns.resolver as dr
import argparse

# init Name Server class
NS = dr.Resolver()

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

	# ArgParser - Define usage
	parser = argparse.ArgumentParser(prog="dns-axfr.py", epilog="DNS Zonetransfer Script", usage="DNS-Zoner.py [options] -d <DOMAIN>", prefix_chars='-', add_help=True)

	# Positional Arguments
	parser.add_argument('-d', action='store', metavar='Domain', type=str, help='Target Domain.\tExample: inlanefreight.htb', required=True)
	parser.add_argument('-n', action='store', metavar='Nameserver', type=str, help='Nameservers separated by a comma.\tExample: ns1.inlanefreight.htb,ns2.inlanefreight.htb')
	parser.add_argument('-v', action='version', version='DNS-AXFR - v1.0', help='Prints the version of DNS-AXFR.py')

	# Assign given arguments 
	args = parser.parse_args()

	# Variables
	Domain = args.d
	NS.nameservers = list(args.n.split(","))

	# Check if URL is given
	if not args.d:
		print('[!] You must specify target Domain.\n')
		print(parser.print_help())
		exit()

if not args.n:
	print('[!] You must specify target nameservers.\n')
	print(parser.print_help())
	exit()

for nameserver in NS.nameservers:
	# attempt to DNS Zone
	AXFR(Domain, nameserver)

# display results
if Subdomains is not None:
	print("--FOUND SUBDOMAINS--")
	
	for subdomain in Subdomains:
		print("{}".format(subdomain))
else:
	print("No subdomains found.")
	exit()	
