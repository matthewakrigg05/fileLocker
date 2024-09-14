class blockingList:

    def __init__(self, filePath):
        self.filePath = filePath

    def getListContents(self):
        fileContents = []

        with open(self.filePath, 'r') as file:
            Lines = file.readlines()

            for line in Lines:
                fileContents.append(line.strip("\n"))

        return fileContents

    def clearListContents(self):
        appsFile = open(self.filePath, 'w')
        appsFile.close()
