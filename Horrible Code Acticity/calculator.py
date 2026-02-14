class Operations:
    def __init__(self):
        self.operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": self.divide  # check for zero
        }

    def calculate(self, a, b, operator):
        return self.operations[operator](a, b)

    def divide(self, a, b):
        if b == 0:
            print("Error dividing by zero")
        return a / b


class UserInput:
    def getInput(self):
        a = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        b = float(input("Enter second number: "))
        return a, b, operator

    def display_result(self, result):
        print("Result:", result)

calculator = Operations()
ui = UserInput()
while exit != "exit":
    try:
        a, b, operator = ui.getInput()
        result = calculator.calculate(a, b, operator)
        ui.display_result(result)
    except:
        print("invalid inputs will restart process")
    exit = input("Type exit to exit or press enter: ").lower()




