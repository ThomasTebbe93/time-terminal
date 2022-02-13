import string
import MFRC522 as mfrc


class ChipReader(object):
    def uidToString(self, uid: list) -> string:
        return "%s%s%s%s" % (
            self.intToHex(uid[0]),
            self.intToHex(uid[1]),
            self.intToHex(uid[2]),
            self.intToHex(uid[3]),
        )

    def intToHex(self, value: int) -> string:
        return f"{value:x}"

    def read(self) -> string:
        MIFAREReader = mfrc.MFRC522()
        (status) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        if status == MIFAREReader.MI_OK:
            print("Card detected")

        (status, uid) = MIFAREReader.MFRC522_Anticoll()

        if status == MIFAREReader.MI_OK:
            print(
                "Card read UID: %s,%s,%s,%s"
                % (hex(uid[0]), hex(uid[1]), hex(uid[2]), hex(uid[3]))
            )
            uidList = [uid[0], uid[1], uid[2], uid[3]]
            result = self.uidToString(uidList)
            print("Card read UID: %s" % (result))
            return result

