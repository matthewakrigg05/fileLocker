import checkFiles
import manipulateList


def main():
    script_running = True
    checkFiles.checkForTxt()

    while script_running:
        print("Options:\n"
              "1: View items in lockedFiles\n"
              "2: Add to list of items\n"
              "3: Remove items\n"
              "4: Clear your list\n"
              "5. Exit program\n")

        ans = input("Which option would you like to take?\n")

        if ans == "1":
            content = checkFiles.lockedFilesContent()
            if len(content) == 0:
                print("You currently have no applications in your list.")
            else:
                print("Currently your list contains:" + ", ".join(content).replace('\n', ''))

        elif ans == "2":
            manipulateList.addToList()

        elif ans == "3":
            manipulateList.removeItem()

        elif ans == "4":
            manipulateList.clearList()

        elif ans == "5":
            script_running = False
            print("Thank you for using fileLocker!")

        else:
            print("Please choose an option by entering a number: 1, 2, 3 4 or 5")


main()