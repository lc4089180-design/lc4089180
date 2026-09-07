#Use ChatGPT or Copilot to generate a Python function that checks if a given string is a valid Indian phone number (should be 10 digits, start with 6-9, and contain only numbers). Test the generated function with three sample inputs and write down if it worked as expected.
def is_valid_indian_phone(phone):
    if len(phone) != 10:
        return False

    if not phone.isdigit():
        return False

    if phone[0] not in "6789":
        return False

    return True


# Test 1
phone1 = "9876543210"
print(phone1, is_valid_indian_phone(phone1))

# Test 2
phone2 = "5123456789"
print(phone2, is_valid_indian_phone(phone2))

# Test 3
phone3 = "98765abc10"
print(phone3, is_valid_indian_phone(phone3))