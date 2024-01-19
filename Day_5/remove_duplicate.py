def remove_duplicates(sorted_array):
    unique_elements = []
    prev_element = None

    for element in sorted_array:
        if element != prev_element:
            unique_elements.append(element)
            prev_element = element

    return unique_elements

input_array = input("Enter a sorted array (space-separated numbers): ")
try:
    input_array = list(map(int, input_array.split()))
    input_array.sort()  # Ensure the array is sorted
except ValueError:
    print("Invalid input. Please enter space-separated numbers.")
    exit()

result_array = remove_duplicates(input_array)

print("Original array:", input_array)
print("Array after removing duplicates:", result_array)

