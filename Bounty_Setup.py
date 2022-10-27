import argparse, os, re

tilde = os.path.expanduser('~')

def main():
	default_path = tilde + '/Documents/' # default file location to save ooutput and file structure

	def argument_parser():
		#This defines the argument parsing module, with this we can start adding arguments, parsing, ETC
		arg_parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Lets help with that common miss organization by starting off the hunt right?\n\nThe goal of this script is to get some basic organization and structure along with automation.\nI hope you enjoy :)\n-YSSVirus')

		domain_group = arg_parser.add_mutually_exclusive_group(required=True)

		#Adding arguments to the script
		domain_group.add_argument('-domain', '--domain', '-host', '--host', help='One of these options is required, This is the target host,\nExample: attcker.hack')
		domain_group.add_argument('-domains', '--domains', '--domain-list', '-dl', help='Here we can choose to instead supply a list of domains')
		arg_parser.add_argument('-directory', '--directory', '-dir', '--dir', default=default_path, help='This is the default directory, we will organize it then save our output\nExample: "~/Documents/Bug_Bounty/HackerOne/"')
		#arg_parser.add_argument('-subdomains', '--subdomains', '--gather-subdomains', help='This option allows us to gather subdomains ( for those wild card targets ;) )\nWe will gather subdomains passively unless given a wordlist.')
		#arg_parser.add_argument('-w', '--w', '-wordlist', '--wordlist', help='Here we can make the subdomain discovery active.')
		arg_parser.add_argument('--subdomain-list', '-sl', '--sl', help='This is where we can give a pre-gathered list of subdomains, we then will organize a file structure dependingly.')

		args = arg_parser.parse_args()#This is the arguments after parsing
		return args # returning arguments so we can call them later

	def single_domain(args):
		os.mkdir("domain")
		os.chdir("domain")		
		target = args.domain
		return target

	def domain_list(args,target,cwd):
		os.mkdir("domains")
		os.chdir("domains")

		for domains in open(cwd + '/' + args.domains, "r"):
			target += domains
			pass

		target = target.splitlines()

		for x in target:
			os.mkdir(x)			
			pass
		return target
	
	args = argument_parser() # this imports our arguments from the function to a variable
	target = ''
	cwd = os.getcwd()
	
	os.chdir(args.directory)
	
	if args.domain != None:
		target = single_domain(args)
	else:
		target = domain_list(args,target,cwd)
		pass
	
	subdomains = ""

	if args.subdomain_list != 'None':
		for subs in open(cwd + '/' + args.subdomain_list, "r"):
			subdomains += subs
			pass
		subdomain_list = subdomains.splitlines()
		cwd = os.getcwd()
		for subdomain in subdomain_list:
			for x in target:
				if subdomain == x:
					pass

				elif re.findall(x,subdomain):
					try:
						os.chdir(cwd + '/' + x)
						os.mkdir(cwd + '/' + x + '/' + subdomain)
						os.chdir(cwd + '/' + x + '/../')
						pass
					except:
						pass

				else:
					pass

	else:
		pass

main()
