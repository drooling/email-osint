import os
from urllib.error import HTTPError

import googlesearch


class Pastebin:
    def __init__(self, email) -> None:
        self.email = email

    def cleanup(self) -> None:
        if os.path.exists(".google-cookie"):
            os.remove(".google-cookie")

    def execute(self) -> None:
        try:
            resp = [_ for _ in googlesearch.search('site:pastebin.com intext:"{0}"'.format(self.email))]
        except HTTPError:
            self.cleanup()
            return print("[ Pastebin Dork ] --> Rate limited\n")
        if not len(resp) > 0:
            self.cleanup()
            return print("[ Pastebin Dork ] --> No results found\n")
        else:
            print("[ Pastebin Dork ] --> \n")
            for result in resp:
                print(f"[ Paste ] --> {result}\n")
        self.cleanup()
