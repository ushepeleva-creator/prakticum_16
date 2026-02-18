from itertools import permutations


def solve():
    """
        Solves a cryptarithmetic puzzle: XOD + XOD + XOD = MAT

        Returns:
            None. Prints the valid equations directly.
        """
    letters = ['Х',
               'О',
               'Д',
               'М',
               'А',
               'Т']
    for perm in permutations(range(10), 6):
        maping = dict(zip(letters, perm))
        X, O, D, M, A, T = maping['Х'], maping['О'], maping['Д'], maping['М'], maping['А'], maping['Т']
        if X == 0 or M == 0:
            continue
        XOD = X * 100 + O * 10 + D
        MAT = M * 100 + A * 10 + T
        if XOD + XOD + XOD == MAT:
            print(f'{XOD}+{XOD}+{XOD}=={MAT}')


solve()
