from unittest import TestCase
import checkFiles


class Test(TestCase):
    def test_checkForTxt(self):
        if not checkFiles.checkForTxt():
            print("File exists")
        else:
            print("File created")

    def test_checkIfProcessRunning(self):
        self.fail()
