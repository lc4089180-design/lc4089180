#Build a Flipkart-style cart total calculator: Given a list of item prices, use a while loop to sum the prices until the total exceeds 1000, then stop and print the subtotal.<br><br><em><strong>Hint:</strong> Use loop control statements to exit the loop once the subtotal goes above 1000.</em>
prices = [250, 300, 200, 400, 150]

subtotal = 0
index = 0

while index < len(prices):
    subtotal += prices[index]

    if subtotal > 1000:
        break

    index += 1

print("Subtotal:", subtotal)