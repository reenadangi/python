class employee:
    raise_amount=1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.email=fname+"."+lname+"@gmail.com"
        self.pay=pay
    def apply_raise(self):
        self.pay=self.pay*self.raise_amount
class developer(employee):
    raise_amount=1.10
    def __init__(self, fname, lname, pay, language):
        super().__init__(fname, lname, pay)
        self.language=language
class Manager(employee):
    def __init__(self, fname, lname, pay, reportees=None):
        super().__init__(fname, lname, pay)
        if reportees is None:
            self.reportees=None
        else:
            self.reportees=reportees

    def add_reportee(self,reportee):
        if reportee not in self.reportees:
            self.reportees.append(reportee)
        
    def remove_reportee(self,reportee):
        if reportee in self.reportees:
            self.remove_reportee(reportee)
    def show_reportees(self):
        for reportee in self.reportees:
            print(f"{reportee.fname} {reportee.lname}")
    
emp=employee("tom","lucas",600000)
print(emp.pay)
emp.apply_raise()
print(emp.pay)

dev1=developer("Reena","Dangi",600000,"Java")
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)
print(developer.raise_amount)
print(dev1.language)

manager1=Manager("Boss","Baby",100000,[dev1])
manager1.show_reportees()
manager1.add_reportee(emp)
manager1.show_reportees()

print(isinstance(manager1,employee))

        
      
