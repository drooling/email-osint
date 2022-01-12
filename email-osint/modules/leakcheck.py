import difflib
import getpass
import json
import os
import pathlib

import requests


class LeakCheck:
	def __init__(self, email: str) -> None:
		self.email = email
		self.key = None
		self.premium = None

	def __validate__(self, cached: bool) -> None:
		resp = requests.get("https://leakcheck.net/api?key={0}&check=valid&type=login".format(self.key))
		data = resp.json()
		if not data.get("success"):
			self.premium = False
		resp = requests.get("https://leakcheck.net/api/public?key={0}&check=valid@gmail.com".format(self.key))
		data = resp.json()
		if not data.get("success"):
			return False
		self.premium = True
		if not cached:
			save = bool(len(difflib.get_close_matches(str(input("Would you like to save this for next time? ")), ['yes', 'y'])) >= 1)
			if save:
				try:
					with open('config/keys.json', 'x+') as dest:
						dest.write(json.dumps({"leakcheck": str(self.key)}, indent=4))
				except FileNotFoundError:
					os.mkdir('config')
					with open('config/keys.json', 'x+') as dest:
						dest.write(json.dumps({"leakcheck": str(self.key)}, indent=4))
				except FileExistsError:
					with open('config/keys.json', 'w+') as dest:
						try:
							existing: dict = json.loads(dest.read())
							existing.update({"leakcheck": str(self.key)})
							dest.write(json.dumps(existing, indent=4))
						except json.decoder.JSONDecodeError:
							dest.write(json.dumps({"leakcheck": str(self.key)}, indent=4))
				print("[ Config ] --> Saved leakcheck API key")
		return True

	def execute(self):
		try:
			with open('config/keys.json', 'r') as loc:
				self.key = json.loads(loc.read()).get("leakcheck", None)
			cached = True
		except FileNotFoundError:
			cached = False
		if not self.key:
			self.key = str(getpass.getpass(prompt="What is your leakcheck.net API key? "))
			cached = False
		if not self.__validate__(cached):
			return print("\n[ Leak Check ] --> Invalid API key\n")
		if self.premium:
			resp = requests.get("https://leakcheck.net/api?key={0}&check={1}&type=email".format(self.key, self.email)).json()
		elif not self.premium:
			resp = requests.get("https://leakcheck.net/api/public?key={0}&check={1}".format(self.key, self.email)).json()
		if resp.get("success"):
			results = set()
			if not self.premium:
				exposed_in = resp.get("sources")
				for breach in exposed_in:
					res = f"\n[ Breach ] --> {breach.get('name')} - {breach.get('date')}\n"
					print(res)
					results.add(res)
			elif self.premium:
				resp = resp.get("result")
				for breach in resp:
					res = f"\n[ Breach ] --> \nCombo: {breach.get('line')}\nLast Exposed: {breach.get('last_breach') or 'Unknown'}\nExposed in: {', '.join(breach.get('sources')) or 'Unknown breach'}\n"
					print(res)
					results.add(res)
				extract = bool(len(difflib.get_close_matches(str(input("Would you like to extract these results to a file? ")), ['yes', 'y'])) >= 1)
				if extract:
					with open(str(os.path.join(str(pathlib.Path.home() / 'Desktop'), str(self.email.split('@')[0] + '.txt'))), 'w+') as destination:
						destination.writelines(results)
						destination.close()
					print("[ Extraction ] --> Results have been saved in a file on your Desktop\n")
		else:
			print("\n[ Leak Check ] --> No breaches found\n")