import requests


class EmailRep:
    def __init__(self, email: str) -> None:
        self.email = email

    def execute(self) -> None:
        resp = requests.get("https://emailrep.io/{0}".format(self.email)).json()
        results = set()
        try:
            print("\n[ Email Reputation ] -->", end='\r', flush=True)
            for key, value in resp.get("details").items():
                if key != "profiles":
                    res = key.replace('_', ' ').title() + ': ' + str(value)
                    print('\n' + res)
                    results.add(res)
            res = "Profiles: " + (', '.join(resp.get("details").get("profiles")) or "None")
            print(res)
            results.add(res)
        except AttributeError:
            print("[ Email Reputation ] --> Error fetching response\n", end='')