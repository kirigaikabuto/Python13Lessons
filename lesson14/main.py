def getWordsFromArr(arr):
    words = []
    for i in arr:
        if i.isalpha():
            words.append(i)
    return words


def getNumbersFromArr(arr):
    numbers = []
    for i in arr:
        if i.isnumeric():
            numbers.append(i)
    return numbers


def getNumbersAndWords(arr):
    elements = []
    for i in arr:
        if i.isnumeric() != True and i.isalpha() != True and i.isalnum():
            elements.append(i)
    return elements


arr = ["sdssdsd", "2", "Hello", "4", "5", "sdsd123", "dsd2323"]
words = getWordsFromArr(arr)
numbers = getNumbersFromArr(arr)
elements = getNumbersAndWords(arr)
print(words)
print(numbers)
print(elements)
