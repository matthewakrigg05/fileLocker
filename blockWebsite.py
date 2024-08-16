def blockWebsites(website):
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'a') as file:
        file.write("127.0.0.1" + " " + website + " www." + website)


def unblockWebsites():
    pass


def webDomainsContent():
    pass

def showBlockedWebsites():
    with open("./webDomains.txt", 'r') as file:
        Lines = file.readlines()
        websites = set()

        for line in Lines:
            strippedLine = line.strip()
            if strippedLine.startswith("#"):
                continue

            websites.add(strippedLine)

        if len(websites) == 0:
            print("You currently have no websites in your list.")
        else:
            print("Currently your list contains: " + ", ".join(websites).replace('\n', ''))

showBlockedWebsites()