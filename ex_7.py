from itertools import permutations


def get_permutations(numbers):
    unique_sorted = sorted(set(numbers))

    return [list(p) for p in permutations(unique_sorted)]


def main():
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
