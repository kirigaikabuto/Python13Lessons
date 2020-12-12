import os

pathToDesktop = "/home/kirigaikabuto/Desktop"
folderName = "example1234"
os.chdir(pathToDesktop)  # cd /home/kirigaikabuto/Desktop
os.mkdir(folderName)  # mkdir /home/kirigaikabuto/Desktop/example123
print(os.getcwd())
