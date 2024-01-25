def max_consecutive_ones(nums):
    max_count = 0
    current_count = 0

    for num in nums:
        if num == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    return max_count

array = list(map(int, input("Enter an array of 0s and 1s separated by spaces: ").split()))

result = max_consecutive_ones(array)
print("Maximum consecutive 1's:", result)
