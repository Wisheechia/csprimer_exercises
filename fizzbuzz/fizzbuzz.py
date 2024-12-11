def fizzbuzz_sum(n):
    num_div_by3 = n // 3
    num_div_by5 = n // 5
    num_div_by15 = n // 15

    return sum(3, num_div_by3) + sum(5, num_div_by5) - sum(15, num_div_by15)


def sum(num, times):
    result = num * times * (times + 1) / 2
    return result


if __name__ == "__main__":
    assert fizzbuzz_sum(999) == 233168
    print('Test passed!')