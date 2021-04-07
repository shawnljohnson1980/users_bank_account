class Bank_Account:
    def __init__(self, int_rate,account_balance,name_input,email_input):
     self.name=name_input
     self.email=email_input
    def add_interest(self):
         self.account_balance=(self.accout_balance*self.account_in_rate)
         print(self.account_balance)
         return self

    def make_deposit(self, amount):
            self.account_balance +=amount
            return self
        
    def venmo (self, amount, payee):
            self.account_balance -=amount
            payee.account_balance +=amount
            return self

    def make_widthdrawl(self, amount):
        self.account_balance -= amount
        return self
class User:
    def __init__(self, name_input, email_input):
        self.name=name_input
        self.email=email_input
        self.account = Bank_Account(int_rate=0.01, balance=0)

shawn = User("Shawn","shawn@mail.com")
andrew= User ("Andrew","andrew@mail.com")    

shawn.account.make_deposit(700).venmo(500, andrew).make_withdrawl(50)
print(f"Shawn's Account balance: ${shawn.account.balance} ")
print(f"Andrews account balance: ${andrew.balance}")
shawn.make_deposit(700).venmo(500, andrew)
print(f"Shawn's Account balance: ${shawn.account.balance} ")
print(f"Andrews account balance: ${andrew.account.balance}")