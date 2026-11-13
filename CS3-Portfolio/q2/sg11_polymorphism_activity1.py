class Patient: # Is the parent class
  def display_patient_type(self):
    print("Patient Type: Regular Patient.")

class SeniorPatient(Patient): # Copies code from Patient Class but overrides with its own code
  def display_patient_type(self):
    print("Patient Type: Senior Citizen")

class PhilhealthPatient(Patient): # Also inherits code from Patient Class but overrides with its own code
  def display_patient_type(self):
    print("Patient Type: PhilHealth Member")

# Example Output:
p1 = Patient()
p1.display_patient_type() # Output: Patient Type: Regular Patient.

p2 = SeniorPatient()
p2.display_patient_type() # Output: Senior Citizen

p3 = PhilhealthPatient()
p3.display_patient_type() # Output: PhilHealth Member
  
    
    
