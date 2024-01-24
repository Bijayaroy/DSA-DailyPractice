def find_missing_element(arr):
    n = len(arr) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    missing_element = expected_sum - actual_sum
    return missing_element

user_input = input("Enter the array elements separated by spaces: ")
arr = list(map(int, user_input.split()))

missing_element = find_missing_element(arr)

print(f"The missing element is: {missing_element}")

