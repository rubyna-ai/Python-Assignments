class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def get_balance(self):
        print(self.name + ": Rs. " + str(self.balance))

ramesh = BankAccount("Ramesh Thapa", "A001", 5000)
sunita = BankAccount("Sunita Karki", "A002", 0)
bikash = BankAccount("Bikash Rai",   "A003", 12000)

sunita.deposit(3000)
bikash.withdraw(15000)
ramesh.withdraw(2000)

ramesh.get_balance()
sunita.get_balance()
bikash.get_balance()