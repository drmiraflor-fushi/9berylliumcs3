class BankAccount:

  #defining variables, no @property used yet
  def __init__(self, account_number, balance):
    self.__account_number = account_number
    self.__balance = balance

  #using @property to bundle pieces of code for easier access / organized process
  @property
  def account_number(self):
    print(account.__number)
    return account.__number

  @property
  def balance(self):
    if balance < 0:
      print("Invalid. Please enter a number that is not negative.")
    else:
      return balance
      
    
    




    
