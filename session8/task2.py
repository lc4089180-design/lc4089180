#Create a function validate_username(username) that returns True only if the username is at least 6 characters, contains only letters and numbers, and does not start with a digit.
def validate_username(username):
    if len(username) < 6:
        return False

    if not username.isalnum():
        return False

    if username[0].isdigit():
        return False

    return True


username = input("Enter username: ")

print(validate_username(username))