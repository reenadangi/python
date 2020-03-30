class emp:
    raise_amount=1.04
    def __init__(self,fname,lname,pay):
        self.fname=fname
        self.lname=lname
        self.email=fname+"."+lname+"@gmail.com"
        self.pay=pay


    def applyraise(self):
        self.pay=self.pay * self.raise_amount    
    
    @classmethod
    def setraiseamount(cls,amout):
        cls.raise_amount=amout

emp1=emp("Reena","Dangi",10000)
print(emp1.email)
emp1.applyraise()
print(emp1.pay)
print(emp.raise_amount)
emp.raise_amount=2
emp1.applyraise()
print(emp1.pay)
emp.setraiseamount(1.2)
emp1.applyraise()
print(emp1.pay)



        
 