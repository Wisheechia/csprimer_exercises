def count_ways_number( n):
    """
    :type n: int
    :rtype: int
    """
    if n == 0 or n == 1:
        return 1
    prev, curr = 1, 1
    for i in range(2, n+1):
        temp = curr
        curr = prev + curr
        prev = temp
    return curr


if __name__ == '__main__':
    expectations = (1, 1, 2, 3, 5, 8)
    for i, x in enumerate(expectations):
        assert count_ways_number(i) == x
    print('Test passed!')