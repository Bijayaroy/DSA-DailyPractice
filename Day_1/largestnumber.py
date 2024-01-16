def find_largest_number(arr):
    if not arr:
        return "Array is empty"

    largest_number = arr[0]

    for num in arr:
        if num > largest_number:
            largest_number = num

    return largest_number

try:
    input_numbers = input("Enter numbers separated by spaces: ")
    array_of_numbers = list(map(int, input_numbers.split()))
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")
    exit()

result = find_largest_number(array_of_numbers)
print(f"The largest number in the array is: {result}")

