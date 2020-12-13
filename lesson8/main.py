import os

pathToDesktop = "/home/kirigaikabuto/Desktop"
os.chdir(pathToDesktop)  # cd pathDoDesktop
mainFileName = "folderLesson8"
if not os.path.isdir(mainFileName):
    os.mkdir(mainFileName)  # mkdir mainFileName
os.chdir(mainFileName)
file1Name = "1"
file2Name = "2"
file3Name = "3"
if not os.path.isdir(file1Name):
    os.mkdir(file1Name)
else:
    print(file1Name + " already created")
if not os.path.isdir(file2Name):
    os.mkdir(file2Name)
else:
    print(file2Name + " already created")
if not os.path.isdir(file3Name):
    os.mkdir(file3Name)
else:
    print(file3Name + " already created")
os.chdir(file1Name)
messageToFile = "Yerassyl"
textFileName = "1.txt"
file = open(textFileName, "w")  # w-write, r - read
file.write(messageToFile)
file.close()
