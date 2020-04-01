# operator overloading
# Dunder methods
class Employee:
    def __init__(self,fname,dept,pay):
        self.fname=fname
        self.dept=dept
        self.pay=pay
    # overloading for print 
    def __repr__(self):
        return f"Name {self.fname}, Department {self.dept}"
    # overloading + /add
    def __add__(self,other):
        return self.pay+other.pay

emp1=Employee("reena","IT",10000)
emp2=Employee("Tom","Sales",30000)
emp3=Employee("Mary","HR",89090)
print(emp1)        
print(emp1+emp2)
# str(emp1)