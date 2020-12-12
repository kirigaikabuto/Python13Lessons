import os

path = os.getcwd()  # pwd
print(path)
os.mkdir("newFOlder")  # mkdir newFolder
desktopPath = "/home/kirigaikabuto/Desktop"
os.chdir(desktopPath)  # cd /home/kirigaikabuto/Desktop
os.mkdir("newFOlder")  # mkdir newFolder
newPath = os.getcwd()  # pdw
print(newPath)
