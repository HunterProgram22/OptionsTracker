import options as opt

test = opt.BuyCallOption("CLNS", "4/20/2018")
#test.option_summary()
print(test.calculate_profit())
