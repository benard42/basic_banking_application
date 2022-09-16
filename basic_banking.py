# 1. Using classes, Create a basic banking application with the following features:

#     1. Create a class called `BankAccount` with the following attributes:

#         1. `account_number` - a string
#         2. `balance` - a float
#         3. `owner` - a string
#         4. `type` - a string


#     The application should have the following functionality:

#     1. Create a new `Bank` object
#     2. Create a new `Customer` object
#     3. Create a new `BankAccount` object
#     4. Add the `BankAccount` object to the `Bank` object
#     5. Add the `BankAccount` object to the `Customer` object
#     6. Print the `Bank` object
#     7. Print the `Customer` object
#     8. Print the `BankAccount` object
#     9. Create a new `Transaction` object
#     10. Add the `Transaction` object to the `BankAccount` object
    

class BankAccount:
        def __init__(self, account_number,balance, owner, type):
            self.account_number = account_number
            self.balance = balance
            self.owner= owner
            self.type= type
        def __repr__(self):
            return f"<BankAccount {self.account_number} {self.balance} {self.owner}{self.type}>"
            
BankAccount = BankAccount("7890","sh 36783","benard","saving")

print(BankAccount.account_number + BankAccount.balance + BankAccount.owner + BankAccount.type)

def Add_account(self, account_number,balance, owner, type):
    print(BankAccount.account_number + BankAccount.balance + BankAccount.owner + BankAccount.type)



    
# 2. Create a class called `Bank` with the following attributes:

# 1. `name` - a string
# 2. `accounts` - a list of `BankAccount` objects

class Bank:
        def __init__(self, name,accounts):
            self.name = name
            self.accounts=accounts
def __repr__(self):
        return f"<Bank {self.name} {self.accounts}>"
Bank = Bank("Bena","saving")
bank = BankAccount()
BankAccount.Add_account("7890","sh 36783","benard","saving")
print(bank.name + BankAccount.accounts )




# 3. Create a class called `Customer` with the following attributes:

#         1. `name` - a string
#         2. `accounts` - a list of `BankAccount` objects

class Customer:
        def __init__(self, name,accounts):
            self.name = name
            self.accounts=accounts
        def __repr__(self):
            return f"<Customer {self.name} {self.accounts}>"
Customer = Customer("Bena","saving")
customer = BankAccount()

BankAccount.Add_account("7890","sh 36783","benard","saving")

print(customer.name + BankAccount.accounts)

    

# 4. Create a class called `Transactions` with the following attributes:
    
#             1. `account` - a `BankAccount` object
#             2. `amount` - a float
#             3. `type` - a string

class Transactions:
        def __init__(self, name,accounts):
            self.name = name
            self.accounts=accounts
        def __repr__(self):
            return f"<Transactions {self.name} {self.accounts}>"
Transactions = Transactions("Bena","saving")
BankAccount= Transactions()
BankAccount.Add_account("7890","sh 36783","benard","saving")

print(Transactions.name + BankAccount.accounts)

