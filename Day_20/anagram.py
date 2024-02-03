def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the lengths of both strings are equal
    if len(str1) != len(str2):
        return False

    # Count character frequencies in str1
    char_count = {}
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Decrement character frequencies in str2
    for char in str2:
        if char in char_count:
            char_count[char] -= 1
        else:
            # If a character in str2 is not in str1, they are not anagrams
            return False

    # Check if all character frequencies are zero
    for count in char_count.values():
        if count != 0:
            return False

    # If all conditions pass, the strings are anagrams
    return True

# Take user input for two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the input strings are anagrams
result = are_anagrams(string1, string2)

if result:
    print(f"{string1} and {string2} are anagrams.")
else:
    print(f"{string1} and {string2} are not anagrams.")
