def find_element_index(arr, num):
    try:
        index = arr.index(num)
        print(f"The element {num} is present at index {index}.")
    except ValueError:
        print(f"The element {num} is not present in the array. Index: -1")


user_input_array = input("Enter the array elements separated by spaces: ")
array= list(map(int, user_input_array.split()))

element = int(input("Enter the element to find: "))

find_element_index(array, element)

