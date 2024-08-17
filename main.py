import blockApps
import checkFiles
import manipulateList
import time


def main():
    checkFiles.checkForFilesTxt()
    checkFiles.checkForWebTxt()
    script_running = True
    txtFileContent = checkFiles.lockedContent()

    while script_running:
        print("Options:\n"
              "1: View items in lockedApps and blocked websites\n"
              " 1b: View items in only lockedApps\n"
              " 1c: View items in only lockedDomains\n"
              "2: Add to list of items\n"
              "3: Remove items\n"
              "4: Clear your lockedApps list\n"
              "5: Clear your lockedDomains list\n"
              "6: Block Apps\n"
              "7: Exit program\n")

        ans = input("Which option would you like to take?\n")

        match ans:
            case "1":
                return manipulateList.showList(txtFileContent)

            case "1b":
                return manipulateList.showBlockedWebsites()

            case "2":
                return manipulateList.addToList(txtFileContent)

            case "3":
                return manipulateList.removeItem(txtFileContent)

            case "4":
                return manipulateList.clearList()

            case "5":
                runningPrograms = []

                for program in txtFileContent:
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
                    print("Starting...\nTo stop this script, simply close it.")

                    while time.time() < timeToLock:
                        blockApps.closeAppIfDetected(txtFileContent)

                    print("Your chosen time to block apps has ended!")

            case "6":
                script_running = False
                print("Thank you for using fileLocker!")

            case _:
                print("Please choose an option by entering a number: 1, 2, 3 4 or 5")


if __name__ == "__main__":
    main()