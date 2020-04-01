class Employee:
    def __init__(self,firstname,lastname):
      self.firstname=firstname
      self.lastname=lastname
      
    def __str__(self):
        return f"First Name: {self.firstname} Last Name:{self.lastname}"
    @property
    def email(self):
        return f"{self.firstname}.{self.lastname}@gmail.com"
    @email.setter
    def email(self,email):
        self.email=email 

emp=Employee("Reena","Dangi")
print(emp)
emp.firstname="Rina"  
print(emp)
print(emp.email)      
emp.email="Ero@gmail.com"