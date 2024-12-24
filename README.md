# Password Generator

## Overview
This Python program generates strong, customizable passwords based on user preferences. The user can specify which types of characters to include (uppercase, lowercase, numbers, symbols) and control the length and number of passwords to generate. The program ensures the generated passwords meet the specified criteria.

---

## Features
- **Customizable Character Pool**: Choose from uppercase letters, lowercase letters, digits, and symbols.
- **Error Handling**: Prevents invalid input such as a requested password length exceeding the available character pool size.
- **Dynamic Interaction**: Asks the user whether to adjust the password length when necessary.
- **Beautiful Output**: Passwords are printed in a clean and user-friendly format.

---

## Requirements
- Python 3.x

---

## How to Use
1. Run the script in a Python environment.
2. Follow the prompts:
   - Decide whether to include uppercase letters, lowercase letters, numbers, and symbols by typing "yes" or "no".
   - Enter the desired password length.
   - Enter the number of passwords to generate.
3. If the requested length exceeds the available character pool, decide whether to adjust the length or exit the program.
4. View your generated passwords in a clean, numbered list.

---

## Example Interaction
```
Include uppercase letters? (yes/no): yes
Include lowercase letters? (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): yes
Enter the desired password length: 10
Enter the number of passwords to generate: 3

Your generated passwords:
==============================
Password 1: qA2]L#zO$v
Password 2: W6d@OF)E+p
Password 3: 8Xs@YLZk%n
==============================
```

---

## Error Handling
- If no character type is selected, the program exits with a message: "You must select at least one character type!"
- If the requested password length exceeds the character pool, the program prompts to adjust the length or exit.

---

## Customization
Modify the script to:
- Add or remove specific characters from the character pools.
- Change the default prompts or add new functionality as needed.

---

## License
This project is open-source and free to use under the MIT License.

