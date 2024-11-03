from typing import List, Tuple, Callable

a = ["Google", "JetBrains", "NVIDIA"]
b = ["Amazon", "Facebook", "Instagram",
     "Tesla", "Microsoft", "Jane Street",
     "Google!", "Googel", "Google LLC",
     "Jet Brains", "jetbrains", "JetTrains",
     "NVDA", "NVIDEA", "Envidia"
 ]

def edit_distance(s1: str, s2: str) -> int:
    """
    Calculate the Optimal String Alignment Distance between two strings: \n
    1 distance operations are: deletion, insertion, substitution, transposition \n
    This function ignores letter cases of passed strings \n
    """
    s1 = s1.lower()
    s2 = s2.lower()
    n, m = len(s1), len(s2)
    memo = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        memo[i][0] = i
    for j in range(m + 1):
        memo[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = memo[i - 1][j - 1]
            else:
                memo[i][j] = 1 + min(memo[i - 1][j], memo[i][j - 1], memo[i - 1][j - 1])
            if i > 1 and j > 1 and s1[i - 2] == s2[j - 1] and s1[i - 1] == s2[j - 2]:
                memo[i][j] = min(memo[i - 2][j - 2] + 1, memo[i][j])
    return memo[n][m]

def fuzzy_search(a: List[str], b: List[str], distance_calc_func: Callable[[str, str], int]) \
        -> List[List[Tuple[str, int]]]:
    """
    Performs fuzzy search on strings from list a in list b \n
    :param distance_calc_func: function for calculating distance between strings (str, str) -> int
    :return: 3 best matches for each string in b with a score in a tuple (str, score)
    """
    result = []
    for name in a:
        tmp1 = list(map(lambda x: (x, distance_calc_func(name, x)), b))
        tmp1.sort(key=lambda x: x[1])
        result.append(tmp1[:3])
    return result

if __name__ == '__main__':
    print(edit_distance("abcd", "acb"))
    print(edit_distance("abc", "acc"))
    print(*fuzzy_search(a, b, edit_distance))