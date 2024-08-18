import blockApps
import blockWebsite
import checkFiles
import manipulateList
import time


def main():
    checkFiles.checkForFilesTxt()
    checkFiles.checkForWebTxt()
    script_running = True

    while script_running:
        print("Options:\n"
              "1: View items in lockedApps and blocked websites\n"
              " 1b: View items in only lockedApps\n"
              " 1c: View items in only lockedDomains\n"
              "2: Add to list of app items\n"
              " 2b: Add to list of websites\n"
              "3: Remove items from list\n"
              " 3b: Remove website from list\n"
              "4: Clear your lists\n"
              " 4b: Clear your lockedApps list\n"
              " 4c: Clear your lockedDomains list\n"
              "5: Block apps and websites\n"
              " 5b: Block only apps\n"
              " 5c: Block only websites\n"
              "6: Exit program\n")

        ans = input("Which option would you like to take?\n")

        match ans:
            case "1":
                manipulateList.showList(checkFiles.lockedContent())

            case "1b":
                manipulateList.showBlockedApps()

            case "1c":
                manipulateList.showBlockedWebsites()

            case "2":
                manipulateList.addToList("textFiles/lockedApps.txt", checkFiles.lockedAppsContent())
                manipulateList.showList(checkFiles.lockedContent())

            case ("2b"):
                manipulateList.addToList("textFiles/lockedDomains.txt", checkFiles.lockedDomainsContent())
                manipulateList.showList(checkFiles.lockedContent())

            case "3":
                manipulateList.removeItem("textFiles/lockedApps.txt", checkFiles.lockedAppsContent())

            case "3b":
                manipulateList.removeItem("textFiles/lockedDomains.txt", checkFiles.lockedDomainsContent())

            case "4":
                manipulateList.clearLists()

            case "4b":
                manipulateList.clearApps()

            case "4c":
                manipulateList.clearWebsites()

            case "5":
                runningPrograms = []

                for program in checkFiles.lockedContent():
                    running = checkFiles.checkIfProcessRunning(program)

                    if running:
                        runningPrograms.append(program)

                if not runningPrograms:
                    print("None of your locked apps are running")
                else:
                    print("Currently you are running: " + ", ".join(runningPrograms) + ".")

                toContinue = input("Are you sure you wish to continue? (Y/N)")

                if toContinue == "Y" or toContinue == "y":
                    timeToLock = time.time() + blockApps.timeToBlock()
                    print("Starting...\n")

                    blockWebsite.blockWebsites(checkFiles.lockedDomainsContent())

                    while time.time() < timeToLock:
                        blockApps.closeAppIfDetected(checkFiles.lockedContent())

                    blockWebsite.unblockWebsites()
                    print("Your chosen time to block apps and websites has ended!\nTo regain access access to these "
                          "websites, close your browser and re-open")

            case "5b":
                runningPrograms = []

                for program in checkFiles.lockedContent():
                    running = checkFiles.checkIfProcessRunning(program)

                    if running:
                        runningPrograms.append(program)

                if not runningPrograms:
                    print("None of your locked apps are running")
                else:
                    print("Currently you are running: " + ", ".join(runningPrograms) + ".")

                toContinue = input("Are you sure you wish to continue? (Y/N)")

                if toContinue == "Y" or toContinue == "y":
                    timeToLock = time.time() + blockApps.timeToBlock()
                    print("Starting...\n")

                    while time.time() < timeToLock:
                        blockApps.closeAppIfDetected(checkFiles.lockedContent())

                    print("Your chosen time to block apps has ended!")

            case "5c":
                toContinue = input("Are you sure you wish to continue? (Y/N)")

                if toContinue == "Y" or toContinue == "y":
                    print("Starting...\n")
                    blockWebsite.blockWebsites(checkFiles.lockedDomainsContent())

                    time.sleep(blockApps.timeToBlock())

                    blockWebsite.unblockWebsites()
                    print("Your chosen time to block apps has ended!\nTo regain access access to these websites, "
                          "close your browser and re-open")

            case "6":
                print("Thank you for using fileLocker!")
                script_running = False

            case _:
                print("Please choose an option by entering one of the given options")

        time.sleep(2.5)


if __name__ == "__main__":
    main()
