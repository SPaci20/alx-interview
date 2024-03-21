#!/usr/bin/python3
def minOperations(n):
    """
    Function to calculate the minimum number of operations
    needed to achieve n 'H' characters in the text file,
    considering only 'Copy All' and 'Paste' operations.

    Args:
        n: The target number of 'H' characters.

    Returns:
        The minimum number of operations needed, or 0 if it's impossible.
    """
    if n == 0:
        return 0

    chars = 1
    operations = 0

    while chars < n:

        if chars * 2 >= n:
            operations += 2
            chars *= 2

        else:
            operations += 2
            chars += chars

    return operations
