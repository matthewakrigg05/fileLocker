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
              "4: Clear your list\n"
              "5: Block Apps\n"
              "6: Exit program\n")

        ans = input("Which option would you like to take?\n")

        if ans == "1":
            manipulateList.showList(txtFileContent)

        # elif ans == "1b":
        #     manipulateList.showBlockedWebsites()

        elif ans == "2":
            manipulateList.addToList(txtFileContent)

        elif ans == "3":
            manipulateList.removeItem(txtFileContent)

        elif ans == "4":
            manipulateList.clearList()

        elif ans == "5":
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

        elif ans == "6":
            script_running = False
            print("Thank you for using fileLocker!")

        else:
            print("Please choose an option by entering a number: 1, 2, 3 4 or 5")


if __name__ == "__main__":
    main()