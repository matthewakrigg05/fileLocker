import subprocess

import checkFiles


def validTimeToBlock(t):
    try:
        int(t)
    except ValueError:
        return False
    else:
        if t <= 0:
            return False
        else:
            return True


def closeAppIfDetected(appsToClose=checkFiles.lockedAppsContent()):
    for apps in appsToClose:
        if apps in str(subprocess.check_output('tasklist')):
            subprocess.call("TASKKILL /F /IM " + apps, shell=True)


def blockWebsites(websitesToBlock=checkFiles.lockedDomainsContent()):
    for website in websitesToBlock:
        with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
            file.write("127.0.0.1" + " " + website + " www." + website)


def unblockWebsites():
    with open("C:\\Windows\\System32\\drivers\\etc\\hosts", 'w') as file:
        file.close()
