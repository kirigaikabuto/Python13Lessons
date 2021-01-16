def checkStr(s):
    s = s.lower()
    check1 = s.isalpha()  # True or False
    if check1:
        return True
    return False


name = input("something:")
checkStr1 = checkStr(name)
if checkStr1:
    print("all ok")
else:
    print("please write only letters")

#kiritio98
#asddasda989