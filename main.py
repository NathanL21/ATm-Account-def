class Account:

  def __init__(self,nameInput,cityInput,accountTypeIn,passwordIn):
    self.name = nameInput
    self.city = cityInput
    self.accountType = accountTypeIn
    self.password = passwordIn
    self.balance = 0

  def getbalance(self):
    return self.balance

  def withdraw(self,ammount):
    self.balance -= ammount

  def deposit(self,ammount):
    self.balance += ammount

myAccount= Account("Nathan","Christiansted","savings","1354")
