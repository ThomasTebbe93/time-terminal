from asyncio.windows_events import NULL
import string
import pip._vendor.requests as requests
import json

from ConfigService import ConfigService


class RequestService:
    def __init__(self):
        config = ConfigService()
        self.baseurl = config.config["API"]["BaseURL"]
        self.login = config.config["Terminal.User.Credentials"]["Login"]
        self.password = config.config["Terminal.User.Credentials"]["Password"]
        self.token = self.getToken()

    def getToken(self) -> string:
        url = "%s/authentication/authenticate" % (self.baseurl)
        payload = {"UserName": self.login, "Password": self.password}
        headers = {
            "content-type": "application/json; charset=UTF-8",
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)

        if r.status_code == 200:
            result = json.decoder(r.json())
            if result.token:
                return result.token
            else:
                print("error trying to authenticate")

    def getUserInfoByChip(self, uid: string) -> json:
        # url = "%s/user/byChipId" % (self.baseurl)
        # headers = {
        #     "content-type": "application/json; charset=UTF-8",
        #     "Authorization": "Bearer %s" % (self.autToken),
        # }

        # r = requests.get(url, headers=headers)
        return json.decoder("{'UserName': 'Thomas Tebbe'}")
