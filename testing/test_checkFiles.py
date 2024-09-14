from unittest import TestCase
import checkFiles


class Test(TestCase):
    def test_checkForTxt(self):
        if not checkFiles.checkTxtFiles():
            print("Files exist")
        else:
            print("Files created")

    def test_checkIfProcessRunning(self):
        self.fail()
