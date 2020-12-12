import os

path = os.getcwd()  # pwd
print(path)
os.mkdir("newFOlder")  # mkdir newFolder
desktopPath = "/home/kirigaikabuto/Desktop"
os.chdir(desktopPath)  # cd /home/kirigaikabuto/Desktop
os.mkdir("newFOlder")  # mkdir newFolder
newPath = os.getcwd()  # pdw
print(newPath)

# создать папку на рабочем столе(desktopFolder) и внутри нее создать еще три папки(1,2,3)
# после создания папки на рабочем столе необходимо поменять путь в котором вы находитесь