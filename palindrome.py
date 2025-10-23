# Program to check if a string is a palindrome

import sys

# Check if Jenkins passes a command-line argument
if len(sys.argv) > 1:
    string = sys.argv[1]
else:
    # Fallback for manual/local runs
    string = input("Enter a string: ")

# Check palindrome
if string.lower() == string[::-1].lower():
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
