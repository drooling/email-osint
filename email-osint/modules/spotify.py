import requests

class Spotify:
    def __init__(self, email: str) -> None:
        self.email = email
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'DNT': '1',
            'Connection': 'keep-alive',
        }

    def execute(self) -> None:
        resp = requests.get("https://spclient.wg.spotify.com/signup/public/v1/account", params={"validate": '1', "email": str(self.email)}, headers=self.headers).json()
        if resp.get("status") == 20:
            return print("[ Spotify ] --> Email linked to Spotify account\n")
        print("[ Spotify ] --> Email NOT linked to Spotify account\n")