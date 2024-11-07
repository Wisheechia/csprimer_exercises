def count_ways_number(n):
    if n <= 2:
        return (1, 1, 2)[n]
    return count_ways_number(n-1) + count_ways_number(n-2) + count_ways_number(n-3)

if __name__ == '__main__':
    expectations = (1, 1, 2, 4, 7, 13)
    for i, x in enumerate(expectations):
        assert count_ways_number(i) == x
    print('Test passed!')