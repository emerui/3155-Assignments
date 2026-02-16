from BankAccount import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number,limit):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self.limit = limit
        self.transfer_made = 0

    def withdraw(self, withdraw):
        if self.transfer_made >= self.limit:
            print("\nAccount reached limit for transfers made\n")
            return
        if self.current_balance - withdraw < self.minimum_balance:
            print("\nYou don't have enough money\n")
            return
        self.current_balance = self.current_balance - withdraw
        self.transfer_made+=1
        print("\n", self.customer_name, "you have withdrawn money:", withdraw)
    def print_customer_information(self):
        super().print_customer_information()
        print("\n You may only transfer money", self.limit, "time(s). You have transferred", self.transfer_made, "time(s).\n")