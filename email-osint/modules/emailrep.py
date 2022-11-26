import requests


class EmailRep:
    def __init__(self, email: str):
        self.email = email

    def execute(self):
        resp = requests.get("https://emailrep.io/{0}".format(self.email)).json()
        try:
            print("[ Email Reputation ] -->")
            for key, value in resp.get("details").items():
                if key != "profiles":
                    print(key.replace("_", " ").title() + ": " + str(value))
            print(
                "Profiles: "
                + (", ".join(resp.get("details").get("profiles")) or "None")
            )
            print("\n")
        except AttributeError:
            print("[ Email Reputation ] --> Error fetching response\n")
