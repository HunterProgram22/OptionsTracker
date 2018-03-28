# A program for stock options.
import time

today = time.strftime("%m/%d/%Y")

class Option(object):
    '''The main class for an option contract.'''
    def __init__(self, ticker, expiration_date, purchase_date=today, shares=100):
        self.purchase_date = purchase_date
        self.expiration_date = expiration_date
        self.stock_symbol = ticker
        self.shares = shares
        self.contract_price = self.set_contract_price()
        self.strike_price = self.set_strike_price()

    def set_strike_price(self):
        self.strike_price = float(input("Enter strike price as a float:\n"))
        return self.strike_price

    def set_contract_price(self):
        self.contract_price = float(input("Enter contract price as float (i.e. 0.05):\n"))
        return self.contract_price

    def contract_cost(self):
        self.contract_cost = self.contract_price*(self.total_contracts*100)
        return self.contract_cost

    def return_data(self):
        print(self.stock_symbol)
        print(self.expiration_date)
        print(self.purchase_date)
        print(self.contract_price)
        print(self.shares)
        print(self.strike_price)


'''
def set_order_type():
    order_type = input("Choose order type of buy or sell:\n")
    return order_type

def set_option_type():
    option_type = input("Choose option type of call or put:\n")
    return option_type

        self.order_type = set_order_type()
        self.option_type = set_option_type()
'''
