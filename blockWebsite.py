def blockWebsites(website):
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'a') as file:
        file.write("127.0.0.1" + " " + website + " www." + website)


def unblockWebsites():
    pass


