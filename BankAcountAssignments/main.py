from CheckingAccount import CheckingAccount
from SavingsAccount import SavingsAccount

student_a = SavingsAccount("Student A", 100, 10, 101, "R1010", .04)
student_b = CheckingAccount("Student B", 90, 0, 102, "R102",3)
student_a.print_customer_information()
student_b.deposit(50)
student_a.withdraw(500)
student_a.withdraw(10)
student_a.print_customer_information()
student_b.print_customer_information()
