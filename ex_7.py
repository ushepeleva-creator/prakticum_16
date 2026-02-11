from itertools import permutations


def get_all_permutations(input_str: str) -> list:
    """
    Get all permutations of a set of natural numbers in lexicographic order.

    Returns:
        list: List of tuples representing all permutations.
    """
    numbers = list(map(int, input_str.split()))

    unique_nums = sorted(set(numbers))

    subsets = []

    for permutation in permutations(unique_nums):
        subsets.append(list(permutation))

    return subsets


def main():
    """
    Main function.
    """
    try:
        input_str = input("Enter natural numbers separated by spaces: ").strip()
        if not input_str:
            print("Error: input cannot be empty!")

        print(get_all_permutations(input_str))

    except ValueError:
        print("Error: all elements must be natural numbers!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()