import string
import requests
import json
import configparser
from datetime import datetime


class RequestService:
    def __init__(self, config: configparser):
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

    def signIn(self, userIdent: string) -> json:
        now = datetime.now()
        current_time = now.strftime("%Y-%d-%m %H:%M:%S")
        url = "%s/dutyHoursBooking/signInByChip" % (self.baseurl)
        payload = {
            "UserIdent": userIdent,
            "BookingTime": current_time,
        }
        headers = {
            "content-type": "application/json; charset=UTF-8",
            "Authorization": "Bearer %s" % (self.autToken),
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)

        if r.status_code == 200:
            return True
        else:
            print("error trying to authenticate")
            return False

    def signOut(self, userIdent: string) -> json:
        now = datetime.now()
        current_time = now.strftime("%Y-%d-%m %H:%M:%S")
        url = "%s/dutyHoursBooking/signOutByChip" % (self.baseurl)
        payload = {
            "UserIdent": userIdent,
            "BookingTime": current_time,
        }
        headers = {
            "content-type": "application/json; charset=UTF-8",
            "Authorization": "Bearer %s" % (self.autToken),
        }
        r = requests.post(url, data=json.dumps(payload), headers=headers)

        if r.status_code == 200:
            return True
        else:
            print("error trying to authenticate")
            return False

    def getUserInfoByChip(self, uid: string) -> json:
        # url = "%s/user/byChipId" % (self.baseurl)
        # headers = {
        #     "content-type": "application/json; charset=UTF-8",
        #     "Authorization": "Bearer %s" % (self.autToken),
        # }

        # r = requests.get(url, headers=headers)
        if uid == "daf8a059":
            return {"UserName": "Thomas Tebbe", "Ident": "f184d9d2-c859-4846-9226-374724382f39"}
        if uid == "8dbe785":
            return {"UserName": "Malte Spiegel", "Ident": "b69dd5a4-950f-4479-a383-ca7cdd5dbdad"}
