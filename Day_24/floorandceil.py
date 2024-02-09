def find_floor_ceiling(arr, x):
    n = len(arr)
    # If x is smaller than the first element in the array
    if x < arr[0]:
        return None, arr[0]
    # If x is greater than the last element in the array
    if x > arr[n - 1]:
        return arr[n - 1], None

    # Binary search to find floor and ceiling
    left, right = 0, n - 1
    floor, ceiling = None, None
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return arr[mid], arr[mid]
        elif arr[mid] < x:
            floor = arr[mid]
            left = mid + 1
        else:
            ceiling = arr[mid]
            right = mid - 1

    return floor, ceiling

arr = []
n = int(input("Enter the number of elements in the array: "))
print("Enter the elements of the array:")
for _ in range(n):
    element = int(input())
    arr.append(element)

x = int(input("Enter the value to find floor and ceiling: "))

floor, ceiling = find_floor_ceiling(arr, x)
print("Floor:", floor)
print("Ceiling:", ceiling)