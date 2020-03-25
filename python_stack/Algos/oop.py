class user:
   
    def __init__(self,name,email):

        self.name=name
        self.email=email
        self.accountBalance=100
        self.interest_rate=0.05
    def display(self):
        print(f"Hi I am {self.name} Amount {self.accountBalance}")
        return self
    def deposite(self,amount):
        self.accountBalance+=amount
        return self
    def withdrawal(self,amount):
        self.accountBalance-=amount
        return self
    def transfer_money(self,other_account,amount):
        self.accountBalance-=amount
        other_account.accountBalance+=amount
        return self
    def yield_interest(self):
        self.accountBalance+=self.accountBalance*self.interest_rate
        return self
        
        
user1=user("Reena","r@go.com")
user1.deposite(300)
user1.display().withdrawal(50).display()

user2=user("Tom","t@go.com")
user1.transfer_money(user2,10).display()
user1.yield_interest().display()
user2.display()



       