#Create a program that takes the price of a Zomato order as input (string), converts it to a float, adds a 10% delivery fee, and prints the final bill amount with two decimal places using f-string formatting.<br><br><em><strong>Hint:</strong> Use float() for conversion and format the output as Rs. 123.45.</em>
price = input ("Enter the Zomato order price: ") 

price = float(price) 

delivery_fee = price * 0.10 

final_bill = price + delivery_fee 

print (f"Final Bill Amount: Rs. {final_bill:.2f}") 