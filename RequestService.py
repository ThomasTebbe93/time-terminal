import string
import requests
import json
import configparser


class RequestService:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        config.sections()
        self.baseurl = config["API"]["BaseURL"]
        self.login = config["Terminal.User.Credentials"]["Login"]
        self.password = config["Terminal.User.Credentials"]["Password"]
        self.token = self.getToken()

    def getToken(self) -> string:
        url = "%s/authentication/authenticate" % (self.baseurl)
        payload = {"UserName": self.login, "Password": self.password}
        headers = {
            "content-type": "application/json; charset=UTF-8",
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)

        if r.status_code == 200:
            result = r.json()
            if result["token"]:
                return result["token"]
            else:
                print("error trying to authenticate")

    def getUserInfoByChip(self, uid: string) -> json:
        # url = "%s/user/byChipId" % (self.baseurl)
        # headers = {
        #     "content-type": "application/json; charset=UTF-8",
        #     "Authorization": "Bearer %s" % (self.autToken),
        # }

        # r = requests.get(url, headers=headers)
        if uid == 'daf8a059':
            return {"UserName": "Thomas Tebbe"}
        if uid == '8dbe785':
            return {"UserName": "Malte Spiegel"}
