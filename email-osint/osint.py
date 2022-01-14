import re
import sys
from argparse import ArgumentParser

from modules import *

regex = re.compile(r"([\w\-\.]+)(?:@)(\w[\w\-]+\.+[\w\-]+)", re.IGNORECASE)

def banner() -> None:
	print("""
                      _ _             _       _   
                     (_) |           (_)     | |  
  ___ _ __ ___   __ _ _| |   ___  ___ _ _ __ | |_ 
 / _ \ '_ ` _ \ / _` | | |  / _ \/ __| | '_ \| __|
|  __/ | | | | | (_| | | | | (_) \__ \ | | | | |_ 
 \___|_| |_| |_|\__,_|_|_|  \___/|___/_|_| |_|\__|
                                                                                               
                                                      
""")

def main():
	parser = ArgumentParser(description="Email-OSINT")
	parser.add_argument("email", help="Target email")
	parser.add_argument("--no-breach", "-nb", default=False, required=False, action="store_true", dest="nobreach", help="Skip the breach check stage")
	args = parser.parse_args()

	banner()

	if not bool(regex.match(args.email)):
		print("That is not a valid email")
		sys.exit(1)

	if not args.nobreach:
		LeakCheck(args.email).execute()

	PsbDump(args.email).execute()
	Pastebin(args.email).execute()
	EmailRep(args.email).execute()
	Spotify(args.email).execute()
	Twitter(args.email).execute()
	Venmo(args.email).execute()
	Snapchat(args.email).execute()

if __name__ == "__main__":
	main()
