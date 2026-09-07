#Use a nested for loop to print a pattern of stars forming a right-angled triangle with 4 rows (like the rating stars you see on Zomato).<br><br><em><strong>Constraint:</strong> Only use for loops and range(), no string multiplication.</em>
for i in range(1, 5):
    for j in range(i):
        print("*", end=" ")
    print()