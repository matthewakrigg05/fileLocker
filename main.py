import checkFiles
import addToList


def main():
    script_running = True
    checkFiles.checkForTxt()

    while script_running:
        print("Options:\n"
              "1: View items in lockedFiles\n"
              "2: Add to list of items\n"
              "3: Remove items\n"
              "4: Start new list\n"
              "5. Exit program\n")

        ans = input("Which option would you like to take?\n")

        if ans == "1":
            addToList.addToList()

        elif ans == "2":
            pass

        elif ans == "3":
            pass

        elif ans == "4":
            pass

        elif ans == "5":
            script_running = False

            print("Thank you for using fileLocker!")

        else:
            print("Please choose an option by entering a number: 1, 2, 3 4 or 5")


main()
