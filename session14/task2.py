#Given a list of usernames from an Instagram-like app, use a list comprehension to create a new list containing only those usernames that start with the letter 'a' or 'A'.
usernames = ["Amit", "rahul", "Anjali", "Priya", "aman", "Kavita"]

a_usernames = [name for name in usernames if name.startswith(("a", "A"))]

print(a_usernames)