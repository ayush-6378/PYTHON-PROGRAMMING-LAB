import pickle
import os

filename = "employee.dat"

# Constraint: Create file and write specific text if it doesn't exist
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG the quick brown fox jumps over the lazy dog\n")

# Main Program
class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary
        
    def __str__(self):
        return f"[{self.empcode}] {self.empname} | Joined: {self.doj} | Salary: {self.salary}"

# 1. Serialization
emp_obj = Employee(1001, "Jane Smith", "2026-01-15", 85000.00)

# Overwriting with 'wb' (write binary) so pickle can format the file correctly
with open(filename, 'wb') as f:
    pickle.dump(emp_obj, f)
print("Employee object serialized successfully.")

# 2. Deserialization
with open(filename, 'rb') as f:
    loaded_emp = pickle.load(f)
    
print("\nDeserialized Employee Data:")
print(loaded_emp)