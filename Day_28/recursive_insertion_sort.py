def recursive_insertion_sort(arr, n):
    # Base case: If array has only one element or is empty
    if n <= 1:
        return

    # Sort first n-1 elements
    recursive_insertion_sort(arr, n-1)

    # Insert last element into sorted array
    last = arr[n-1]
    j = n-2

    # Move elements of arr[0..i-1], that are greater than last,
    # to one position ahead of their current position
    while j >= 0 and arr[j] > last:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = last


# Take user input for array elements
arr = input("Enter the array elements separated by spaces: ").split()
arr = [int(x) for x in arr]  # Convert input strings to integers

n = len(arr)
recursive_insertion_sort(arr, n)
print("Sorted array:", arr)
