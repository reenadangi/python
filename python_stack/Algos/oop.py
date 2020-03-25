class user:
   
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.accountBalance=100
    def display(self):
        print(f"Hi I am {self.name} Amount {self.accountBalance}")
        return self
    def make_withdrawal(self,amount):
        self.accountBalance-=amount
        return self
    def transfer_money(self,other_account,amount):
        self.accountBalance-=amount
        other_account.accountBalance+=amount
        return self
        
user1=user("Reena","r@go.com")
user1.display().make_withdrawal(50).display()
user2=user("Tom","t@go.com")
user2.transfer_money(user1,10).display()




       