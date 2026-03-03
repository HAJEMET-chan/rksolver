from math import factorial
from numpy import sum as np_sum


def permutation_to_index(permutation):
    index = 0
    for i in range(1, len(permutation)):
        index += np_sum(permutation[:i]>permutation[i]) * factorial(i)
    return index

def orientation_to_index(orientation, base):
    value = 0
    for d in orientation:
        value = value * base + d
    return value