class BankAccount:

  # defining variables, no @property used yet
  def __init__(self, account_number, balance):
    self.__account_number = account_number
    self.__balance = balance

  # using @property to bundle pieces of code for easier access / organized process; this is the getter
  @property
  def get_account_number(self):
    return self.__account_number

  @property
  def get_balance(self):
    return self.__balance
    
  # using the setter function of the built-in function of @property to further define balance & account number
  @set_account_number(new_account_number)
  def account_number(self):
    account_number = "17"
    print("Account Number:", account_number)
    
  @set_balance(new_balance): 
  def balance(self):
        balance = "1893"
    if balance < 0:
        print("Invalid. Please enter a number that is not negative.")
      else:
        return balance

      
      




    
