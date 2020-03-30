# regular methods - pass instance as argument
# class methods - pass class as argument
# static methods - pass nothing as argument
import datetime 
class employee:
    no_of_emp=0
    def __init__(self,name,department,pay):
        self.name=name
        self.department=department
        self.pay=pay
        employee.no_of_emp+=1

    # regular method, passes self as argument 
    def apprasial(self,amount):
        self.pay=self.pay + amount

    # Class methods can be use as alternative constructor, i,t passes class itself
    @classmethod
    def total_emp(cls):
        return cls.no_of_emp
    @staticmethod
    def is_work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        else:
            return True

emp1=employee("reena","IT",60000)
emp2=employee("Mark","Sales",30000)
print(employee.total_emp())
my_date=datetime.date(2020,3,12)
print(employee.is_work_day(my_date))
    