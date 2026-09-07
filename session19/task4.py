#Modify the following code so that it only prints email addresses ending with '.in' from a list of emails using regex:<br><br>emails = ['user1@gmail.com', 'friend@yahoo.in', 'test123@outlook.in', 'hello@company.com']<br><br><em><strong>Constraint:</strong> Use the re module and avoid using list comprehensions for filtering.</em>
import re

emails = [
    "user1@gmail.com",
    "friend@yahoo.in",
    "test123@outlook.in",
    "hello@company.com"
]

pattern = r"^[\w.-]+@[\w.-]+\.in$"

for email in emails:
    if re.match(pattern, email):
        print(email)