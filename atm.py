
class Atm(object):
    def __init__(self, card_number, pin_number, balance):
        self.card_number = card_number
        self.pin_number = pin_number
        self.balance = balance

    def checkBalance(self):
        return self.balance

    def cashWithdrawal(self, amount):
        self.balance = self.balance - amount
        return self.balance

    def cashDeposit(self, amount):
        self.balance = self.balance + amount
        

account = Atm(8409574346721198, 1234, 500)
print(account.card_number)
account.cashDeposit(1000)
balance = account.checkBalance()
print(balance)
balance = account.cashWithdrawal(200)
print(balance)