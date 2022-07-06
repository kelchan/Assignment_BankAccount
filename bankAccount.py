from code import interact


class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self
        else:
            print( "Insufficient Funds: Charging a $5 fee" )
            self.balance -= 5
            return self

    def display_account_info(self):
        # print( f"Interest Rate: {self.int_rate}" )
        print( f"Balance: ${self.balance}" )
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance = (self.balance * self.int_rate) + self.balance
            return self
        return self

    def print_all_info( self ): 
        self.display_account_info()
        print( f"Interest Rate: {self.int_rate}" )

account_kelvin = BankAccount( 0.01, 0 )
account_random = BankAccount( 0.02, 0 )

account_kelvin.deposit( 100 ).deposit( 200 ).deposit( 300 ).withdraw( 100 ).yield_interest().display_account_info()
account_random.deposit( 100 ).deposit( 100 ).withdraw( 50 ).withdraw( 50 ).withdraw( 100 ).withdraw( 100 ).yield_interest().display_account_info().print_all_info()