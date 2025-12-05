# palindrome.py
import sys

# If argument is passed (Jenkins), use it
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    # Normal user input
    text = input("Enter a string: ")

# Reverse
rev = text[::-1]

# Check palindrome
if text == rev:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
