def ask_quantity_of_apple_and_orange():
    applesQuantity = int(input("Quantity of apples:"))
    orangesQuantity =int(input("Quantity of oranges:"))
    return applesQuantity, orangesQuantity

def compute_total_amount():
    amount_= apples*applesQ + oranges*orangesQ
    return amount_

def displayOutput(amount_):
    print(f"The total amount is {amount_}.")

#ask for apples and oranges you want to buy 
applesQ, orangesQ = ask_quantity_of_apple_and_orange()
#input prices of apples and oranges
apples = 20
print(f"price of apple is = {apples}")
oranges = 25
print(f"price of orange is = {oranges}")
#compute total price
amount = compute_total_amount()
# 5. display the total amount in the ff. format : The total amount is ___.
displayOutput(amount)