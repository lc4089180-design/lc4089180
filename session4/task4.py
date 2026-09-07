#Write a program that takes a user's Paytm wallet balance and the amount they want to pay. Use conditional statements to check if the payment can be processed (balance >= amount). Print 'Payment Successful' or 'Insufficient Balance' accordingly.<br><br><em><strong>Constraint:</strong> Do not use the input() function more than twice.</em>
balance = float(input("Enter your Paytm wallet balance: "))
amount = float(input("Enter the amount you want to pay: "))

if balance >= amount:
    print("Payment Successful")
else:
    print("Insufficient Balance")