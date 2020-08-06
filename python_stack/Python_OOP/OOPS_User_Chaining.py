class User:
    
    def __init__(self, user_name,email):
        self.user_name=user_name
        self.email=email
        self.account_balance=0
    def make_deposit(self,amount):
         self.account_balance+=amount
         return self
# make_withdrawal(self, amount) - have this method decrease the user's 
# balance by the amount specified
    def make_withdrawal(self, amount):
         self.account_balance-=amount
         return self
# display_user_balance(self) 
    def display_user_balance(self):
        print(self.user_name, "balance is:", self.account_balance)
        return self
# transfer_money(self, other_user, amount)
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        # make_deposit(other_user,amount)
        other_user.make_deposit(amount)
        return self
    


# Working with class objects 
first_user= User("Reena","reena@gmail.com")
other_user=User("Pankaj","pc.gmail.com")

first_user.make_deposit(1000).make_deposit(1000).make_withdrawal(200).display_user_balance().transfer_money( other_user, 300).display_user_balance()
other_user.display_user_balance()

