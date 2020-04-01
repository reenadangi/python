# In Python, getters and setters are not the same as those in other object-oriented programming languages. Basically, the main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Private variables in python are not actually hidden fields like in other object oriented languages. Getters and Setters in python are often used when:
# We use getters & setters to add validation logic around getting and setting a value.
# To avoid direct access of a class field i.e. private variables cannot be accessed directly or modified by external user.
class Employee:
    def __init__(self): 
        self._age = 0
        
        # function to get value of _age 
        def get_age(self): 
            print("getter method called") 
            return self._age 
        
        # function to set value of _age 
        def set_age(self, a): 
            print("setter method called") 
            self._age = a 
    
        # function to delete _age attribute 
        def del_age(self): 
            del self._age 
     
        age = property(get_age, set_age, del_age)  
  
mark = Employee() 
  
mark.age = 10
  
print(mark.age) 