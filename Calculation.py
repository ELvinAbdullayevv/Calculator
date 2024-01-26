def calculate():
    number_1 = input("First number ")
    number_2 = input("Second number ")

    if not number_1.isdigit() or not number_2.isdigit():
        print("Numbers are invalid")
        return

    c = int(number_1)
    b = int(number_2)

    calculation = input("Please choose calculation + - / * ")
    if calculation not in ("+", "-", "*", "/"):
        print("Calculation is invalid")
        return

    def plus():
        print("{} + {} = ".format(c, b), c + b)

    def minus():
        print("{} - {} = ".format(c, b), c - b)

    def multiply():
        print("{} * {} = ".format(c, b), c * b)

    def division():
        print("{} / {} = ".format(c, b), c / b)

    match calculation:
        case "+":
            plus()
        case "-":
            minus()
        case "*":
            multiply()
        case "/":
            division()


calculate()