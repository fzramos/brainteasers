"""
    Find the number with the most digits.

    If two numbers in the argument array have the same number of digits, return the first one in the array.
"""

# quick first attempt
def find_longest(arr):
    strs = list(map(str, arr))
    # without key max would see string 4 as greater than string 1000
    return int(max(strs, key = len))

def find_longest_best(arr):
    return max(arr, key=lambda x: len(str(x)))