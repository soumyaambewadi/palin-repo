# palindrome_check.py
# Program to check if a string is a palindrome

# Taking user input
string = input("Enter a string: ")

# Converting to lowercase and checking
if string.lower() == string[::-1].lower():
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
