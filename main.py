class Bank :

  def __init__(self, Account_NO, balance ):
    self.Account_NO = Account_NO
    self.balance = balance

  # debit method
  def credit (self, amount): 
    self.balance +=amount
    print("Rs." , amount , "has been credited to your account")
    print("The balance is", self.balance)
  # credit method
  def debit (self, amount):
    self.balance -= amount
    print("Rs." , amount , "has been debited from your account")
    print("The balance is", self.balance)


  def check_balance (self):
    print(f" The balance is {self.balance}")

account1 = Bank(123456, 10000)
account1.credit(5000)
account1.debit(1500)
