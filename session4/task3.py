#Create a Python program that checks if a Zomato order is eligible for free delivery: if the total amount is greater than or equal to 299, print 'Free Delivery', else print 'Delivery Charges Apply'.
total_amount = float(input("Enter your order amount: "))

if total_amount >= 299:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")