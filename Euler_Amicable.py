cache_sum_proper_divisors = dict()


def proper_divisors(number: int) -> int:
    yield 1
    square_root = int(number ** 0.5)
    if number % square_root == 0:
        yield square_root
    for i in range(2, square_root + 1):
        if number % i == 0:
            yield i
            yield int(number / i)


def sum_proper_divisors(number: int) -> int:
    if number in cache_sum_proper_divisors:
        return cache_sum_proper_divisors[number]
    cache_sum_proper_divisors[number] = sum(proper_divisors(number))
    return cache_sum_proper_divisors[number]


def amicable(numbers: (int, int)) -> bool:
    if numbers[0] == numbers[1]:
        return False
    if sum_proper_divisors(numbers[0]) == numbers[1] and sum_proper_divisors(numbers[1]) == numbers[0]:
        return True
    return False


def gen_amicable(number: int) -> (int, int) or None:
    pair = (number, sum_proper_divisors(number))
    if amicable(pair):
        return pair