znak = ""

while znak != "0":
    znak = input("znak:")
    if znak == "0":
        break
    a = int(input("number1:"))
    b = int(input("number2:"))
    output = 0
    if znak == "+":
        output = a + b
    elif znak == "-":
        output = a - b
    elif znak == "/":
        output = a / b
    elif znak == "*":
        output = a * b
    print(output)
