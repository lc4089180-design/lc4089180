#Build a password strength checker function check_password_strength(password) that returns 'Weak', 'Medium', or 'Strong' based on these rules: Weak if less than 6 characters, Medium if at least 6 and contains letters and numbers, Strong if it also contains at least one special character (!@#$%^&*).
def check_password_strength(password):
    if len(password) < 6:
        return "Weak"

    has_letter = False
    has_number = False
    has_special = False

    special_characters = "!@#$%^&*"

    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_number = True
        elif char in special_characters:
            has_special = True

    if has_letter and has_number and has_special:
        return "Strong"
    elif has_letter and has_number:
        return "Medium"
    else:
        return "Weak"


password = input("Enter password: ")

print("Password Strength:", check_password_strength(password))