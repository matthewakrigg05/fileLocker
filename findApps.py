from windows_tools.installed_software import get_installed_software

for software in get_installed_software():
    print(software)
