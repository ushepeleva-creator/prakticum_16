from itertools import combinations


def get_all_subsets(numbers):
    """
    Generate all possible subsets of unique numbers.
    
    Args:
        numbers: List of integers (may contain duplicates)
    
    Returns:
        List of lists, where each inner list is a subset
    """
    unique = sorted(set(numbers))
    result = []
    for r in range(len(unique) + 1):
        for combo in combinations(unique, r):
            result.append(list(combo))
    return result


def main():
    try:
        numbers = list(map(int, input("Enter numbers: ").split()))
        
        if not numbers:
            print("Error: input cannot be empty!")
            return
            
        subsets = get_all_subsets(numbers)
        print(subsets)
        
    except ValueError:
        print("Error: all elements must be integers!")


if __name__ == "__main__":
    main()

