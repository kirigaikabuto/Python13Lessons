def checkForUsername(s):
    s = s.lower()
    check1 = s.isnumeric()
    if check1:
        return False
    check2 = s.isalnum()
    if check2:
        return True
    return False


username = input("username:")
check = checkForUsername(username)
if check:
    print("ok")
else:
    print("error")
