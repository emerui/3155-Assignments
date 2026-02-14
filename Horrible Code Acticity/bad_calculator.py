class Operations:
    def __init__(self, operator, a, b):
        self.operator = operator
        self.a = a
        self.b = b
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b
    def divide(self, a, b):
        return a / b
    def calculate(self):
            if self.operator == "+":
                return self.add(self.a, self.b)
            elif self.operator == "-":
                return self.subtract(self.a, self.b)
            elif self.operator == "*":
                return self.multiply(self.a, self.b)
            elif self.operator == "/":
                if self.b == 0:
                    print("Error by division of zero")
                    return 0
                return self.divide(self.a, self.b)

while True:
    operator = input("Enter operator (+, -, *, /) or 'exit' to exit: ")

    if operator.lower() == "exit":
        break
    if operator not in ["+", "-", "*", "/"]:
        print("Invalid operator. Try again.")
        continue

    a = input("Enter first numerical number: ")
    b = input("Enter second numerical number: ")
    try:
        float(a)
        float(b)
    except ValueError:
        print("Invalid numerical numbers. Try again.")
        continue
    ops = Operations(operator, float(a), float(b))
    print("Result:", ops.calculate())
