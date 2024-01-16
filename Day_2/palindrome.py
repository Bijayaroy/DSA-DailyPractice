def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_s = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_s == cleaned_s[::-1]

user_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_input):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
