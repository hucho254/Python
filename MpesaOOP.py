from abc import ABC, abstractmethod
# encaplsulation
class Account:
    def __init__(self, account_id,holder_name , account_balance):
        self.holder_name = holder_name
        self.account_id = account_id
        self.account_balance = account_balance
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if amount <=self.account_balance:
           self.account_balance -= amount
        else:
            print("Insufficient balance")
    def balance(self):
        return self.account_balance

    def name(self):
        return self.holder_name
# INHERITANCE
class Customer(Account):
    def __init__(self, holder_name, account_id, account_balance, phone_number):
        super().__init__(holder_name,account_id,account_balance)
        self.phone_number = phone_number
# Polymorphism
class Transaction:
    def __init__(self, transaction_amount):
        self.transaction_amount = transaction_amount
    def execute(self, account):
        pass
class DepositTransaction(Transaction):
    def execute(self, account):
        account.deposit(self.transaction_amount)
class WithdrawTransaction(Transaction):
    def execute(self, account):
        account.withdraw(self.transaction_amount)
# abstractions
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class MpesaPaymentSystem(Payment):
    def process_payment(self, amount):
        print(f"processing mpesa payment of {amount}")
# Example usage
mpesa = MpesaPaymentSystem()
account1=Customer("Huncho", 1 ,2000 ,739560933)
deposit=DepositTransaction(450)
withdraw=WithdrawTransaction(1780)
deposit.execute(account1)
withdraw.execute(account1)
print(f"The balance of {account1.name()} is {account1.balance()}")
# example usage 2
mpesa = MpesaPaymentSystem()
account2=Customer("Felix", 2 ,3000 ,737960698)
deposit=DepositTransaction(700)
withdraw=WithdrawTransaction(2000)
deposit.execute(account2)
withdraw.execute(account2)
print(f"The balance of {account2.name()} is {account2.balance()}")
