def blockWebsites():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts") as file:
        file.write("127.0.0.1" + " " + "youtube.com\n")

def unblockWebsites():
    pass

blockWebsites()