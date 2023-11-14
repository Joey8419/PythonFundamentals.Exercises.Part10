class Person:

    def __init__(self, first, last):
        # Assign unique ID to person
        self.id = Person.next_id
        # Increment the next_id  for the next instance
        Person.next_id += 1

        # Assign first and last name in instance variables
        self.first_name = first
        self.last_name = last


class Account:

    def __init__(self, number, account_type, owner, balance):
        self.number = number
        self.type = account_type
        self.owner = owner
        self.balance = balance


class Bank:

    def __init__(self):
        # Initialize bank object with an empty list of customers and accounts
        self.accounts = []
        self.accounts = []

    def add_customer(self, customer):
        # Add customer to bank
        self.customer.append(customer)

    def add_account(self, account):
        # Add account to bank
        self.accounts.append(account)

    def remove_account(self, account):
        # Remove account from bank
        self.accounts.remove(account) if account in self.accounts else print("Account is not found")

    def deposit(self, account, amount):
        # Deposit money into account
        account.balance += amount
        print(f"${amount} deposited into account {account.number} has new balance of: ${account.balance} ")

    def withdraw(self, account, amount):
        # Withdraw money from account
        if account.balance >= amount:
            account.balance -= amount
            print(f"${amount} withdrawn from account {account.number} now has a new balnce of: {account.balance}")
        else:
            print("YOU BROKE BIH")

    def balance_inquiry(self, account):
        # Retrieves balance from particular account
        print(
            f"YOU BROKE BIH. I DON'T KNOW WHY YOU CHECKING account {account.number}: YOUR BALANCE IS ${account.balance}")
