import requests

class Twitter:
    def __init__(self, email: str) -> None:
        self.email = email

    def execute(self) -> None:
        resp = requests.get("https://api.twitter.com/i/users/email_available.json", params={"email": str(self.email)}).json()
        if resp.get("taken"):
            return print("[ Twitter ] --> Email linked to Twitter account\n")
        print("[ Twitter ] --> Email NOT linked to Twitter account\n")