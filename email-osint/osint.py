import re
import sys

from modules import *

regex = re.compile(r"([\w\-\.]+)(?:@)(\w[\w\-]+\.+[\w\-]+)", re.IGNORECASE)

def main(email: str):
	EmailRep(email).execute()
	LeakCheck(email).execute()
	Spotify(email).execute()
	Twitter(email).execute()
	Venmo(email).execute()

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("You must only specify a email")
		sys.exit(1)
	if not bool(regex.match(sys.argv[1])):
		print("That is not a valid email")
		sys.exit(1)
	main(sys.argv[1])
