import blockApps
import checkFiles
import manipulateList


def main():
    script_running = True
    checkFiles.checkForTxt()
    txtContent = checkFiles.lockedFilesContent()

    while script_running:
        print("Options:\n"
              "1: View items in lockedFiles\n"
              "2: Add to list of items\n"
              "3: Remove items\n"
              "4: Clear your list\n"
              "5: Block Apps\n"
              "6: Exit program\n")

        ans = input("Which option would you like to take?\n")

        if ans == "1":
            manipulateList.showList(txtContent)

        elif ans == "2":
            manipulateList.addToList(txtContent)

        elif ans == "3":
            manipulateList.removeItem(txtContent)

        elif ans == "4":
            manipulateList.clearList()

        elif ans == "5":
            blockApps.timeToBlock()
            runningPrograms = []

            for program in txtContent:
                running = checkFiles.checkIfProcessRunning(program)

                if running:
                    runningPrograms.append(program)

            if not runningPrograms:
                print("None of your locked apps are running")
            else:
                print("Currently you are running: " + ", ".join(runningPrograms) + ".")

            blockApps.closeAppIfDetected(runningPrograms)

            """
            check if the apps are running -> if are then close
            """

        elif ans == "6":
            script_running = False
            print("Thank you for using fileLocker!")

        else:
            print("Please choose an option by entering a number: 1, 2, 3 4 or 5")


main()