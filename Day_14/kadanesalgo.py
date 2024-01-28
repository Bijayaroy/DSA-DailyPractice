def kadanes_algorithm(arr):
    maxEndingHere = maxSoFar = arr[0]
    start = end = 0
    currentStart = 0

    for i in range(1, len(arr)):
        if arr[i] > maxEndingHere + arr[i]:
            maxEndingHere = arr[i]
            currentStart = i
        else:
            maxEndingHere = maxEndingHere + arr[i]

        if maxEndingHere > maxSoFar:
            maxSoFar = maxEndingHere
            start = currentStart
            end = i

    return maxSoFar, arr[start:end+1]

def main():
    
    try:
        input_str = input("Enter the array elements separated by spaces: ")
        arr = list(map(int, input_str.split()))
    except ValueError:
        print("Invalid input. Please enter integers separated by spaces.")
        return

    if not arr:
        print("Empty array. Please enter at least one element.")
        return

    result, subarray = kadanes_algorithm(arr)
    print("Maximum Subarray Sum:", result)
    print("Maximum Subarray:", subarray)

if __name__ == "__main__":
    main()

