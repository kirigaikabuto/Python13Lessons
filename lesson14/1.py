def isEmpty(s):
    if len(s) == 0:
        return True
    return False


def isLetterAndNumbers(s):
    if s.isalnum():
        return True
    return False


def checkAll(s):
    check1 = isEmpty(s)
    if check1:
        return False
    check2 = isLetterAndNumbers(s)
    if not check2:
        return False
    return True


word = "adsadsdad"
check = checkAll(word)
print(check)
