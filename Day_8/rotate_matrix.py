def rotate_matrix_90_clockwise(matrix):
    rows, cols = len(matrix), len(matrix[0])
    rotated_matrix = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated_matrix[j][rows - 1 - i] = matrix[i][j]

    return rotated_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))

        matrix = []
        for i in range(rows):
            row = list(map(int, input(f"Enter row {i+1} (space-separated values): ").split()))
            if len(row) != cols:
                raise ValueError("Number of columns entered doesn't match the specified number.")
            matrix.append(row)

        print("\nOriginal Matrix:")
        print_matrix(matrix)

        rotated_matrix = rotate_matrix_90_clockwise(matrix)

        print("\nRotated Matrix (90 degrees clockwise):")
        print_matrix(rotated_matrix)

    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()

