from itertools import combinations


def get_k_subsets(numbers, k):
    """
    Generate all K-element subsets of unique numbers.

    Args:
        numbers: List of integers (may contain duplicates)
        k: Size of subsets to generate

    Returns:
        List of lists, where each inner list is a K-element subset
    """
    unique = sorted(set(numbers))
    return [list(combo) for combo in combinations(unique, k)]


def main():
    try:
        numbers = list(map(int, input("Enter numbers: ").split()))
        if not numbers:
            print("Error: input cannot be empty!")
            return

        k = int(input("Enter K (subset size): "))

        if k < 0 or k > len(set(numbers)):
            print(f"Error: K must be between 0 and {len(set(numbers))}")
            return

        print("=" * 50)
        print(get_k_subsets(numbers, k))

    except ValueError:
        print("Error: all elements must be integers!")


if __name__ == "__main__":
    main()
