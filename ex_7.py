from itertools import permutations


def get_permutations(numbers):
    """
    Generate all permutations of unique numbers in lexicographic order.

    This function takes a list of numbers, removes duplicates, sorts them,
    and returns all possible permutations as lists.

    Args:
        numbers (list): A list of integers (may contain duplicates).

    Returns:
        list: A list of lists, where each inner list represents a unique
              permutation of the sorted unique input numbers.
              Returns an empty list if input is empty.
    """
    unique_sorted = sorted(set(numbers))

    return [list(p) for p in permutations(unique_sorted)]


def main():
     """
    Main function to handle user input and display permutations.
    Returns:
        None. Prints the result directly to console.
    """
    try:

        numbers = list(map(int, input("Enter numbers: ").split()))

        if not numbers:
            print("Error: input cannot be empty!")
            return

        print(get_permutations(numbers))

    except ValueError:
        print("Error: all elements must be integers!")


if __name__ == "__main__":
    main()

