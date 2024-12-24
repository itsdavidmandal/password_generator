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

    # Check if the requested length is valid
    while length > len(all):
        print(f"Error: Password length ({length}) exceeds the size of the character pool ({len(all)}).")
        change_length = input("Do you want to change the password length? (yes/no): ").strip().lower()
        if change_length == "yes":
            length = int(input(f"Enter a new password length (max {len(all)}): "))
        else:
            print("Exiting program. Adjust your input and try again.")
            exit()

    # Generate and print passwords
    print("\nYour generated passwords:\n" + "=" * 30)
    for i in range(1, amount + 1):
        password = "".join(random.sample(all, length))
        print(f"Password {i}: {password}")
    print("=" * 30)
