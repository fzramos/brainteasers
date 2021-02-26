"""
    Given an integer as input, can you round it to the next (meaning, "higher") multiple of 5?

    Examples:

    input:    output:
    0    ->   0
    2    ->   5
    3    ->   5
    12   ->   15
    21   ->   25
    30   ->   30
    -2   ->   0
    -5   ->   -5
"""

# quick, inital solution
def round_to_next5(n):
    remain = n%5
    if remain == 0:
        return n
    n += 5-remain
    return n


# Refactored, efficient solution
def round_to_next5(n):
    return n + (5 - n) % 5