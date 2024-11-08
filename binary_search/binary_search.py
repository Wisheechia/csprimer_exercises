def correct_binary_search(n, array):
    low, high = 0, len(array) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == n: return mid
        if array[mid] < n: low = mid + 1
        else: high = mid - 1
    return -1


if __name__ == '__main__':
    cases = (
        (-1, [-1, 43, 56, 87, 100], 0),
        (4, [-5, -3, 0, 4, 20], 3),
        (5, [-5, -3, 0, 4, 20], -1)
    )
    
    for n, array, expectation in cases:
        assert correct_binary_search(n, array) == expectation
    print("Test passed!")