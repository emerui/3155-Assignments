from BankAccount import BankAccount
class SavingsAccount(BankAccount):
    #savings account needs interest
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.interest = interest

    def apply_interest(self):
        interest = self.interest * self.current_balance
        self.current_balance += interest
        print("\n", self.customer_name, "Interested added! New balance: ", self.current_balance, "\n")
    def print_customer_information(self):
        super().print_customer_information()
        print("\nYour current interest rate is: ", self.interest, "\n")