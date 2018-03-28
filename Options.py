# A program for stock options.
import time

today = time.strftime("%m/%d/%Y")

class Option(object):
    '''The main class for an option contract.'''
    def __init__(self, stock_symbol, expiration_date, purchase_date=today, contracts = 1, shares=100):
        self.stock_symbol = stock_symbol
        self.expiration_date = expiration_date
        self.purchase_date = purchase_date
        self.total_contracts = contracts
        self.shares_per_contract = shares
        self.total_shares = self.total_contracts*self.shares_per_contract
        self.strike_price = self.set_strike_price()
        self.contract_price = self.set_contract_price()

    def set_strike_price(self):
        self.strike_price = float(input("Enter strike price as a float (i.e. 5.00):\n"))
        return self.strike_price

    def set_contract_price(self):
        self.contract_price = float(input("Enter contract price as float (i.e. 0.05):\n"))
        return self.contract_price

    def contract_cost(self):
        self.contract_cost = self.contract_price*(self.total_shares)
        return self.contract_cost


class BuyCallOption(Option):
    '''A subclass option that is an option to buy the stock at the strike strike_price
    on the expiration date.'''
    def __init__(self, ticker, expiration_date):
        Option.__init__(self, ticker, expiration_date)
        self.breakeven_price = self.calculate_breakeven_price()
        self.maximum_loss = self.calculate_maximum_loss()

    def calculate_breakeven_price(self):
        self.breakeven_price = ((self.strike_price*(
                self.total_shares))+self.contract_cost())/(self.total_shares)
        return self.breakeven_price

    def calculate_maximum_loss(self):
        self.maximum_loss = self.contract_price*self.total_shares
        return self.maximum_loss

    def option_summary(self):
        print("You have the option to buy " + str(self.total_shares) + " shares of " +\
        str(self.stock_symbol) + "\non " + str(self.expiration_date) + " at a price of $" +\
        str(self.strike_price) + " per share.")
        print("Your breakeven price is: $" + str(self.breakeven_price))
        print("Your maximum loss is: $" + str(self.maximum_loss))
