# A program for stock options.

def set_order_type():
    order_type = input("Choose order type of buy or sell:\n")
    return order_type

def set_option_type():
    option_type = input("Choose option type of call or put:\n")
    return option_type

def set_contract():
    contract_price = float(input("Enter contract price as float (i.e. 0.05): \n"))
    total_contracts = int(input("Enter total number of contracts as integer:\n"))
    return contract_price, total_contracts

class Option(object):
    '''The main class for an option contract.'''
    def __init__(self, ticker):
        self.purchase_date = None
        self.expiration_date = None
        self.stock_symbol = ticker
        self.order_type = set_order_type()
        self.option_type = set_option_type()
        self.contract_price, self.total_contracts = set_contract()

    def contract_cost(self):
        self.contract_cost = self.contract_price*(self.total_contracts*100)
        return self.contract_cost

    def return_data(self):
        print(self.stock_symbol)
        print(self.order_type)
        print(self.option_type)
        print(self.contract_price)
        print(self.total_contracts)
