import requests


class EmailRep:
    def __init__(self, email: str) -> None:
        self.email = email

    def execute(self) -> None:
        resp = requests.get("https://emailrep.io/{0}".format(self.email)).json()
        results = []
        try:
            print("[ Email Reputation ] -->", end='\r', flush=True)
            for key, value in resp.get("details").items():
                if key != "profiles":
                    res = key.replace('_', ' ').title() + ': ' + str(value)
                    results.append(res)
            res = "Profiles: " + (', '.join(resp.get("details").get("profiles")) or "None")
            results.append(res)
            print('\n')
            [print(resu) for resu in results]
            print('\n')
        except AttributeError:
            print("[ Email Reputation ] --> Error fetching response\n")