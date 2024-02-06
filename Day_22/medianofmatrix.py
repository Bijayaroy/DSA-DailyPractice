def findMedian(matrix):
    # Flatten the matrix into a single array
    flattened = [element for row in matrix for element in row]
    
    # Sort the flattened array
    flattened.sort()
    
    # Find the median
    n = len(flattened)
    if n % 2 == 0:
        # If the length of the array is even, median is the average of two middle elements
        median = (flattened[n // 2 - 1] + flattened[n // 2]) / 2
    else:
        # If the length of the array is odd, median is the middle element
        median = flattened[n // 2]
    
    return median

def main():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))

    matrix = []
    print("Enter the elements of the matrix row-wise:")

    for i in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("Median of the matrix:", findMedian(matrix))

if __name__ == "__main__":
    main()
