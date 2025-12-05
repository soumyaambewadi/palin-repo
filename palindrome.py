# palindrome.py

# Prompt user to enter a string
text = input("Enter a string: ")

# Reverse the string
reversed_text = text[::-1]

# Check if palindrome
if text == reversed_text:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")
