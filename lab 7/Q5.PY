# Dictionary 1: Items and their prices per unit
prices = {
    "apple": 50,
    "milk": 30,
    "bread": 40,
    "eggs": 10
}

# Dictionary 2: Items and the quantity purchased
quantities = {
    "apple": 2,
    "milk": 3,
    "bread": 1
}

total_bill = 0

print("--- Bill Details ---")

# Loop through the items in the quantities dictionary
for item in quantities:
    # Get the quantity from dictionary 2
    qty = quantities[item]
    
    # Get the matching price from dictionary 1
    price = prices[item]
    
    # Calculate cost for this specific item
    item_cost = qty * price
    print(item, ":", qty, "x", price, "=", item_cost)
    
    # Add to the grand total
    total_bill = total_bill + item_cost

print("--------------------")
print("Total Bill Amount: Rs.", total_bill)