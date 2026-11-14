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

  def calculate_bill(self):
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
print("Hospital Billing System")
print("------------------------")
patients = [
  Patient("Rohan Kishibe", 1000.0),
  SeniorPatient("Joseph Joestar", 1000.0),
  PhilhealthPatient("Giorno Giovanna", 1000.0)
]
  
for patient in patients:
  print(f"Patient Name: {patient.get_name()}")
  patient.display_patient_type()
  print(f"Original Bill: {patient.get_bill_amount():,.2f} pesos.")
  print(f"Final Bill: {patient.calculate_bill():,.2f} pesos.\n")
  
