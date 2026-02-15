class BankAccount:
    bank_title = "UNC Charlotte Banks"
    def __init__(self, customer_name, current_balance, minimum_balance):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

    def deposit(self, add):
        self.current_balance = self.current_balance + add

    def withdraw(self, withdraw):
        if self.current_balance-withdraw < self.minimum_balance:
            print("\nyou don't have enough money\n")
        else:
            self.current_balance = self.current_balance - withdraw

    def print_customer_information(self):
        print("\nName: ", self.customer_name)
        print("\n Current balance: ", self.current_balance)
        print("\nYou cannot go below: ", self.minimum_balance)
        print("\nYou are banking with: ", self.bank_title)

student_a = BankAccount("Student A", 100, 10)
student_b = BankAccount("Student B", 90, 0)
student_a.print_customer_information()
student_b.deposit(50)
student_a.withdraw(500)
student_a.withdraw(10)
student_a.print_customer_information()
student_b.print_customer_information()

