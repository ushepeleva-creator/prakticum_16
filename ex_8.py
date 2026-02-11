from itertools import combinations


def get_all_subsets(input_str: str) -> list:
    """
    Generate all possible subsets of a set of natural numbers.

    Args:
        input_str (str): String containing natural numbers separated by spaces.

    Returns:
        list: List of tuples, where each tuple represents a subset.
    """
    numbers = list(map(int, input_str.split()))

    unique_nums = sorted(set(numbers))

    subsets = []

    for r in range(len(unique_nums) + 1):
        for combo in combinations(unique_nums, r):
            subsets.append(list(combo))

    return subsets


def main():
    """
    Main function.
    """
    try:
        input_str = input("Enter natural numbers separated by spaces: ").strip()

        if not input_str:
            print("Error: input cannot be empty!")

        else:
            print(get_all_subsets(input_str))

    except ValueError:
        print("Error: all elements must be natural numbers!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()