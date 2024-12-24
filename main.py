import random

# Define character pools
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case = upper_case.lower()
digits = "0123456789"
symbols = "!@#$%^&*()_+[]:;<>,./?"

# Prompt user for inclusion of character types
upper = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
lower = input("Include lowercase letters? (yes/no): ").strip().lower() == "yes"
nums = input("Include numbers? (yes/no): ").strip().lower() == "yes"
syms = input("Include symbols? (yes/no): ").strip().lower() == "yes"

# Build the character pool
all = ""
if upper:
    all += upper_case
if lower:
    all += lower_case
if nums:
    all += digits
if syms:
    all += symbols

# Check if the pool is empty
if not all:
    print("You must select at least one character type!")
else:
    # Password settings
    length = int(input("Enter the desired password length: "))
    amount = int(input("Enter the number of passwords to generate: "))

    # Generate and print passwords
    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)
