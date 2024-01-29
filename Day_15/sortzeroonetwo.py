def sortColors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

user_input = input("Enter an array of 0s, 1s, and 2s separated by spaces: ")
nums = list(map(int, user_input.split()))

sortColors(nums)

print("Sorted array:", nums)