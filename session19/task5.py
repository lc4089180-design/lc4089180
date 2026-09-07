#Use ChatGPT or Copilot to generate a Python regex pattern that matches valid Indian phone numbers (starting with 7, 8, or 9 and exactly 10 digits). Test the pattern by checking three sample numbers and print whether each is valid.
import re

pattern = r"^[789]\d{9}$"

phone_numbers = [
    "9876543210",
    "8123456789",
    "6123456789"
]

for number in phone_numbers:
    if re.match(pattern, number):
        print(number, "- Valid")
    else:
        print(number, "- Invalid")