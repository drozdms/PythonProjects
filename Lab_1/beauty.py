def are_beauties(a, b):
    return '0' not in f"{a}{b}"


def get_beauties(n):
    for i in range(1, n//2):
        if are_beauties(i, n-i):
            return i, n-i

