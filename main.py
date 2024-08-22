import block
import checkFiles
import manipulateList
import time


def main():
    checkFiles.checkForFilesTxt()
    checkFiles.checkForWebTxt()
    script_running = True

    while script_running:
        pass
        # case "1b":
        #     manipulateList.showBlockedApps()
        #
        # case "1c":
        #     manipulateList.showBlockedWebsites()
        #
        # case "2":
        #     manipulateList.addToList("textFiles/lockedApps.txt", checkFiles.lockedAppsContent())
        #     manipulateList.showList(checkFiles.lockedContent())
        #
        # case ("2b"):
        #     manipulateList.addToList("textFiles/lockedDomains.txt", checkFiles.lockedDomainsContent())
        #     manipulateList.showList(checkFiles.lockedContent())
        #
        # case "3":
        #     manipulateList.removeItem("textFiles/lockedApps.txt", checkFiles.lockedAppsContent())
        #
        # case "3b":
        #     manipulateList.removeItem("textFiles/lockedDomains.txt", checkFiles.lockedDomainsContent())
        #
        # case "4":
        #     manipulateList.clearLists()
        #
        # case "4b":
        #     manipulateList.clearApps()
        #
        # case "4c":
        #     manipulateList.clearWebsites()
