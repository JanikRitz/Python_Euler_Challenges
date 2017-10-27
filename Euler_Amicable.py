'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

'''
from enum import Enum

cache_sum_proper_divisors = dict()
cache_number_form = dict()


def proper_divisors(number: int):
    divisors = set()
    divisors.add(1)
    square_root = int(number ** 0.5)
    if number % square_root == 0:
        divisors.add(square_root)
    for i in range(2, square_root + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(int(number / i))
    return divisors


def sum_proper_divisors(number: int) -> int:
    if number in cache_sum_proper_divisors:
        return cache_sum_proper_divisors[number]
    cache_sum_proper_divisors[number] = sum(proper_divisors(number))
    return cache_sum_proper_divisors[number]


class NumberForm(Enum):
    PERFECT = 0
    DEFICIENT = -1
    ABUNDANT = 1


def number_form(number: int):
    if number in cache_number_form:
        return cache_number_form[number]
    elif number == sum_proper_divisors(number):
        cache_number_form[number] = NumberForm.PERFECT
    elif number > sum_proper_divisors(number):
        cache_number_form[number] = NumberForm.DEFICIENT
    else:
        cache_number_form[number] = NumberForm.ABUNDANT
    return cache_number_form[number]


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
