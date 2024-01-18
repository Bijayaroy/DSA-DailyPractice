def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


user_array = list(map(int, input("Enter elements separated by spaces: ").split()))

selection_sort(user_array)

print("Sorted array:", user_array)

