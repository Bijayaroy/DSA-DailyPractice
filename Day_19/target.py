def find_indices(arr, target):
    found = False
    indices = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                found = True
                indices = [i, j]
                break

        if found:
            break

    return found, indices


arr_str = input("Enter the array of integers (comma-separated): ")
arr = [int(num) for num in arr_str.split(',')]

target = int(input("Enter the target value: "))

result, indices = find_indices(arr, target)

if result:
    print("Yes")
    print("Indices are:", indices)
else:
    print("No such indices found.")
