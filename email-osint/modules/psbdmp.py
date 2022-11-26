import requests

class PsbDump:
    def __init__(self, email):
        self.email = email

    def execute(self):
        resp = requests.get("https://psbdmp.ws/api/v3/search/{0}".format(self.email)).json()
        if not resp.get("count") > 0:
            print("[ Pastebin Dump ] --> No results found\n")
        else:
            print("[ Pastebin Dump ] --> \n")
            for result in resp.get("data"):
                print(f"[ Paste ] --> https://pastebin.com/{result.get('id')}\n")