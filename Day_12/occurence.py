def find_single_occurrence(numbers):
    occurrence_dict = {}

    # Count occurrences of each number
    for num in numbers:
        if num in occurrence_dict:
            occurrence_dict[num] += 1
        else:
            occurrence_dict[num] = 1

    # Find numbers with only one occurrence
    result = [key for key, value in occurrence_dict.items() if value == 1]

    return result

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    numbers = list(map(int, user_input.split()))

    result = find_single_occurrence(numbers)

    print("Numbers that appear once:", result)

if __name__ == "__main__":
    main()

