from itertools import combinations


def get_k_subsets(input_str: str, k: int) -> list:
    """
    Generate all K-element subsets of a set of natural numbers.

    Args:
        input_str (str): String containing natural numbers separated by spaces.
        k (int): Size of subsets to generate.

    Returns:
        list: List of tuples, where each tuple represents a K-element subset.
    """
    numbers = list(map(int, input_str.split()))
    unique_numbers = sorted(set(numbers))

    subsets = []

    for combo in combinations(unique_numbers, k):
        subsets.append(list(combo))

    return subsets


def main():
    """
    Main function.
    """
    try:
        input_str = input("Enter natural numbers separated by spaces:").strip()

        if not input_str:
            print("Error: input cannot be empty!")
        else:
            k = int(input("Enter K (subset size): ").strip())

            print("=" * 50)
            print(get_k_subsets(input_str, k))

    except ValueError:
        print("Error: all elements must be natural numbers!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
