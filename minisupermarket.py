print("---Welcome to the Supermarket---")

available_items = {"milk": 50, "bread": 30, "eggs": 10, "fruits": 20}
print("Available items and their prices:", available_items)

total_bill = 0

while True:
    item = input("Enter the item you want to buy: ").lower()

    if item in available_items:
        quantity = int(input("Enter quantity: "))
        price = available_items[item] * quantity
        total_bill += price
        print("Added to cart. Cost =", price)
    else:
        print("Item not available")

    choice = input("Do you want to buy another item? (yes/no): ")
    if choice.lower() != "yes":
        break

print("The total bill is:", total_bill)
print("Thank you for shopping with us!")
        
        