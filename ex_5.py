def sieve_of_eratostenes(n):
    """
        Finds all prime numbers in the range [2, n) using the Sieve of Eratosthenes algorithm.

        Parameters:
        n (int): The upper bound of the range (exclusive).

        Returns:
        set: A set of prime numbers from 2 up to n-1.
             Returns an empty set if n <= 2.

        """
    if n <= 2:
        return set()
    numbers = set(range(2, n))
    i = 2
    while i ** 2 < n:
        if i in numbers:
            nums = set(range(i ** 2, n, i))
            numbers -= nums
        i += 1
    return numbers


n = int(input())
print(sieve_of_eratostenes(n))


if __name__ == "__main__":
    main()
