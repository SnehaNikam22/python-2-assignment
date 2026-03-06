# Creating the parent class named  person class
class person:
    def __init__(self,name,age):
        self ._name = name
        self ._age = age

# Creating the subclass and inheriting the properties from the parent class
class Employee(person):
    def __init__(self, name, age,emp_ID):
        super().__init__(name, age)      # Call parent constructor
        self ._emp_ID = emp_ID

# Creating another subclass named Manager inherited from both person and Employee
class Manager(Employee):
    def __init__(self,name,age,emp_ID,Email):
       super().__init__(name,age,emp_ID)   # call Employee constructor
       self._Email = Email

# Creating objects
P = person("Sneha", 18)
E = Employee("Sneha", 18, 1304)
M = Manager("Sneha", 18, 1304,"abcd@gmail.com")

print("As your data is protected it wont print the data as your output!!")
print("To print your information we will apply print statement")

# Applying print statement for printing the information
print("Name:",P._name, "Age:",P._age)
print("Employee name:",E._name, "Employee age:",E._age,"Employee ID:",E._emp_ID)
print("Manager name:",M._name,"Manager age:",M._age,"Manager ID:",M._emp_ID,"Manager Email:",M._Email)