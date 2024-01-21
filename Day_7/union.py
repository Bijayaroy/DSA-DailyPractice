def find_union(arr1, arr2):
    union_set = set(arr1) | set(arr2)
    union_list = sorted(list(union_set))
    return union_list

arr1 = list(map(int, input("Enter elements of the first sorted array (space-separated): ").split()))

arr2 = list(map(int, input("Enter elements of the second sorted array (space-separated): ").split()))

# Finding and displaying the union of the two arrays
result = find_union(arr1, arr2)
print("Union of the two sorted arrays:", result)
