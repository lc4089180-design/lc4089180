#Create a script that takes a cricket player's runs and strike rate as input and prints 'Excellent', 'Good', or 'Needs Improvement' based on these rules: if runs > 50 and strike rate > 120, print 'Excellent'; if runs > 30 and strike rate > 100, print 'Good'; else print 'Needs Improvement'.<br><br><em><strong>Hint:</strong> Use if-elif-else statements for the conditions.</em>
runs = int(input("Enter player's runs: "))
strike_rate = float(input("Enter strike rate: "))

if runs > 50 and strike_rate > 120:
    print("Excellent")
elif runs > 30 and strike_rate > 100:
    print("Good")
else:
    print("Needs Improvement")