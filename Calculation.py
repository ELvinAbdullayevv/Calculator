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




# Another with Decorator
number1 = input()
number2 = input()
calculation = input()


def calculator(func):
    def calc_progress(a, b):
        a = int(a)
        b = int(b)
        if a == 0 or b == 0:
            print("The result equal to 0")
            return
        else:
            print("Calculating...")
            return func(a, b)

    return calc_progress


@calculator
def plus(a, b):
    print(a + b)


@calculator
def multiply(a, b):
    print(a * b)


@calculator
def division(a, b):
    print(a / b)


@calculator
def minus(a, b):
    print(a - b)


match calculation:
    case "+":
        plus(number1, number2)
    case "-":
        minus(number1, number2)
    case "/":
        division(number1, number2)
    case "*":
        multiply(number1, number2)