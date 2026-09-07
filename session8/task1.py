#Write a Python function is_valid_email(email) that checks if a given string is a valid email address using string methods (like find, count, startswith, endswith) and returns True or False.<br><br><em><strong>Hint:</strong> Check for exactly one '@', at least one '.', and that '@' is not at the start or end.</em>
def is_valid_email(email):
    if email.count("@") != 1:
        return False

    if email.startswith("@") or email.endswith("@"):
        return False

    if email.find(".") == -1:
        return False

    return True


email = input("Enter email: ")

print(is_valid_email(email))