from xxlimited_35 import Null


class BankAccount:
    bank_title = "UNC Charlotte Banks"
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance
        self._account_number = account_number #_ is protected
        self.__routing_number = routing_number #__ is private

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
