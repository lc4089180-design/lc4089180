#Refactor the following code to use a lambda function inside the map() method to add 100 reward points to each user's points in a list: users = [120, 340, 560, 80]. Print the new list of points.<br><br><em><strong>Constraint:</strong> Do not use a for loop.</em>
users = [120, 340, 560, 80]

new_points = list(map(lambda points: points + 100, users))

print(new_points)