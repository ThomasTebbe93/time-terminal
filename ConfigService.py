import configparser
import string


class ConfigService:
    def __init__(self) -> function:
        self.paser = configparser.ConfigParser()
        self._readConfig()

    def _readConfig(self, path: string) -> function:
        self.config = self.paser.read("config.ini")
