class Patient: # Is the parent class
  def __init__(self, name: str, bill_amount: float):
    self._name = name
    self._bill_amount = bill_amount

  def get_name(self):
    return self._name

  def set_name(self, name: str):
    self._name = name

  def get_bill_amount(self):
    return self._bill_amount

  def set_bill_amount(self, bill_amount: float):
    self._bill_amount = bill_amount

  def calculare_bill)self):
    return self._bill_amount
    
  def display_patient_type(self):
    print("Patient Type: Regular Patient.")

class SeniorPatient(Patient): # Copies code from Patient Class but overrides with its own code (for the display, and calculation of final bill / discount)
  def calculate_bill(self): # Applies the 20% discount for senior citizens
    return self.get_bill_amount() * 0.80

  def display_patient_type(self):
    print("Patient Type: Senior Citizen")

class PhilhealthPatient(Patient): # Also inherits code from Patient Class but overrides with its own code (for the display, and calculation of final bill / discount)
  def calculate_bill(self): # Applies the 15% discount for Philhealth members
    return self.get_bill_amount() * 0.85
  
  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")

# Example Output:
p1 = Patient("Rohan Kishibe", 1000.0)
p1.display_patient_type() # Output: Patient Type: Regular Patient.
print(f"Name: {p1.get_name()}, Final Bill: {p1.calculate_bill()}\n")

p2 = SeniorPatient("Joseph Joestar", 1000.0)
p2.display_patient_type() # Output: Senior Citizen
print(f"Name: {p2.get_name()}, Final Bill: {p2.calculate_bill()}\n") # Displays the final bill with the 20% discount

p3 = PhilhealthPatient()
p3.display_patient_type("Giorno Giovanna", 1000.0) # Output: PhilHealth Member
print(f"Name: {p3.get_name()}, Finall Bill: {p3.calculate_bill()}\n") # Displays the final bill with the 15% discount
    
    
