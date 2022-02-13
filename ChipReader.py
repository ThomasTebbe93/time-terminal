import string
import RPi.GPIO as GPIO
import MFRC522 as mfrc
import signal


class ChipReader(object):
    def end_read(signal, frame):
        global continue_reading
        print("Ctrl+C captured, ending read.")
        GPIO.cleanup()

    def uidToString(uid: list) -> string:
        return "%s%s%s%s" % (
            f"{hex(uid[0]):02}",
            f"{hex(uid[1]):02}",
            f"{hex(uid[2]):02}",
            f"{hex(uid[3]):02}",
        )

    def read(self) -> string:
        signal.signal(signal.SIGINT, self.end_read)
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
            result = self.uidToString(uid)
            print("Card read UID: %s" % (result))
            return result
