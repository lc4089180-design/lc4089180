#Simulate a Zomato-style order retry: Use a while loop to keep asking the user to enter 'yes' to confirm their food order, and stop only when the user types 'yes'.
order_confirmed = ""

while order_confirmed != "yes":
    order_confirmed = input("Enter 'yes' to confirm your food order: ")

print("Order Confirmed!")