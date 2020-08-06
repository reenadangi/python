class User:
    
    def __init__(self, user_name,email):
        self.user_name=user_name
        self.email=email
        self.account=BankAccount(0)
    
    def make_deposit(self,amount):
         self.account.deposit(amount)
         return self
# make_withdrawal(self, amount) - have this method decrease the user's 
# balance by the amount specified
    def make_withdrawal(self, amount):
         self.account.withdraw(amount)
         return self
# display_user_balance(self) 
    def display_user_balance(self):
        print(self.user_name, "balance is:",  self.account.account_balance)
        return self
# transfer_money(self, other_user, amount)
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        # make_deposit(other_user,amount)
        other_user.make_deposit(amount)
        return self
    
class BankAccount:
    def __init__(self,amount=0):
        self.account_balance=amount
        self.interest_rate=0.01
# deposit(self, amount) - increases the account balance by the given amount  
    def deposit(self, amount):
        self.account_balance+=amount
        return self
    # withdraw(self, amount)
    def withdraw(self, amount):
        print("self.account_balance-amount",self.account_balance-amount)
        if(self.account_balance-amount+5>0):
            self.account_balance-=5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.account_balance-=amount
        return self
    # display_account_info(self)
    def display_account_info(self):
        print("Balance is" ,self.account_balance)
        return self
    # yield_interest(self)
    def yield_interest(self):
        self.account_balance+=self.account_balance*self.interest_rate
        return self


# Working with class objects 
first_user= User("Reena","reena@gmail.com")
other_user=User("Pankaj","pc.gmail.com")



first_user.make_deposit(1000).make_deposit(1000).make_withdrawal(200).display_user_balance().transfer_money( other_user, 300).display_user_balance()
other_user.display_user_balance()


acc1=BankAccount()
acc2=BankAccount()

acc1.deposit(100).deposit(200).deposit(1000).withdraw(100).yield_interest().display_account_info()

acc2.deposit(100).deposit(100).display_account_info().withdraw(100).withdraw(100).display_account_info()