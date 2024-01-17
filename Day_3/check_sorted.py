user_input = input("Enter elements of the array separated by spaces: ")
user_array = list(map(int, user_input.split()))

sorted_array = sorted(user_array)

# Check if the array is sorted
if user_array == sorted_array:
    print("True.")
else:
    print("False.")

