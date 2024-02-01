def set_zeros(matrix):
    rows, cols = len(matrix), len(matrix[0])

    zero_positions = []

    # Find the positions of zeros in the matrix
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_positions.append((i, j))

    # Set entire rows and columns to zero based on zero_positions
    for position in zero_positions:
        row, col = position

        # Set entire column to zero
        for i in range(rows):
            matrix[i][col] = 0

        # Set entire row to zero
        for j in range(cols):
            matrix[row][j] = 0

    return matrix

def get_matrix_from_user():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix = []
    print("Enter the elements of the matrix:")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
            row.append(element)
        matrix.append(row)

    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

user_matrix = get_matrix_from_user()

print("\nOriginal Matrix:")
print_matrix(user_matrix)

result_matrix = set_zeros(user_matrix)

print("\nMatrix after setting zeros:")
print_matrix(result_matrix)
