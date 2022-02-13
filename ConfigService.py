import configparser
import string


class ConfigService:
    def __init__(self):
        self.paser = configparser.ConfigParser()
        self._readConfig()

    def _readConfig(self, path: string):
        self.config = self.paser.read("config.ini")
