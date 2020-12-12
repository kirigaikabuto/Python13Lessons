import os

absolutePath = os.getcwd()
directories = os.listdir()
for file in directories:
    fullPath = absolutePath + "/" + file
    print(fullPath)
