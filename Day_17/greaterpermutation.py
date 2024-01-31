def next_permutation(a):
    i = len(a) - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1

    if i == -1:
        return None
        
    j = len(a) - 1
    while a[j] <= a[i]:
        j -= 1

    a[i], a[j] = a[j], a[i]

    a[i + 1:] = reversed(a[i + 1:])

    return a

user_input = input("Enter a permutation (comma-separated numbers): ")
permutation = [int(x) for x in user_input.split(",")]

next_permutation_result = next_permutation(permutation)

if next_permutation_result:
    print("Next lexicographically greater permutation:", next_permutation_result)
else:
    print("No greater permutation exists.")
