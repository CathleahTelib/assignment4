def money_and_price():
    moneyQuantity = int(input("Enter amount of money you have:"))
    applePrice = float(input("Price of apple:"))
    return moneyQuantity,applePrice

def compute_and_output():
    possiblePurchase = moneyQ // appleP
    moneyChange = moneyQ % appleP
    print(f"You can buy {possiblePurchase:.0f} apples and your change is {moneyChange:.2f} pesos.") 

# steps
# 1. ask money that you have and save to variable
moneyQ,appleP = money_and_price()
# 2. compute total purchase and total change and display in the ff. format: You can buy _____ apples and your change is _____ pesos.
totalAmount = compute_and_output()