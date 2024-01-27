def longest_subarray_with_sum(arr, k):
    start = 0
    end = 0
    current_sum = 0
    max_length = 0
    result = None

    while end < len(arr):
        current_sum += arr[end]

        while current_sum > k:
            current_sum -= arr[start]
            start += 1

        if current_sum == k and (end - start + 1) > max_length:
            max_length = end - start + 1
            result = arr[start:end+1]

        end += 1

    return result

n = int(input("Enter the size of the array: "))

arr = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    arr.append(element)

k = int(input("Enter the target sum: "))

result = longest_subarray_with_sum(arr, k)

if result:
    print("Longest subarray with sum", k, ":", result)
else:
    print("No subarray found with sum", k)

