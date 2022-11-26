import json

import requests
from bs4 import BeautifulSoup


class Snapchat:
	def __init__(self, email: str):
		self.email = email
		self.xsrf = None
		self.web_client = None

	def get_cookies(self):
		resp = requests.get("https://accounts.snapchat.com").text
		soup = BeautifulSoup(resp, 'html.parser')
		self.xsrf = soup.find("div", attrs={'id': 'login-root'}).attrs.get("data-xsrf")
		self.web_client = soup.find("div", attrs={'id': 'login-root'}).attrs.get("data-web-client-id")

	def execute(self):
		self.get_cookies()
		headers = {
			"Host": "accounts.snapchat.com",
			"User-Agent": "Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19",
			"Accept": "*/*",
			"X-XSRF-TOKEN": self.xsrf,
			"Accept-Encoding": "gzip, late",
			"Content-Type": "application/json",
			"Connection": "close",
			"Cookie": "xsrf_token=" + self.xsrf + "; web_client_id=" + self.web_client
		}
		data = str(json.dumps({"email": self.email, "app": "BITMOJI_APP"}))
		resp = requests.post("https://accounts.snapchat.com/accounts/merlin/login", data=data, headers=headers)
		if resp.status_code != 204:
			try:
				resp = resp.json()
				if resp.get("hasSnapchat"):
					return print("[ Snapchat ] --> Email linked to Snapchat account\n")
				print("[ Snapchat ] --> Email NOT linked to Snapchat account\n")
			except:
				print("[ Snapchat ] --> Error fetching data\n")
