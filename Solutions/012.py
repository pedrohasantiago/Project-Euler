"""Get triangle number with more than a certain number of divisors."""
# What is the value of the first triangle number to have over five
# hundred divisors?
# (Link: https://projecteuler.net/problem=12)

from math import sqrt
from typing import Iterable

def generate_triangle_number() -> Iterable[int]:
    curr = 1
    while True:
        # The n-th triangular number is the sum of all integers until n,
        # so it is basically a arithmetic progression of ratio 1:
        yield curr * (curr + 1) // 2
        curr += 1

def count_divisors(num: int) -> int:
    num_divisors = 0
    for i in range(1, int(sqrt(num))):
        if num % i == 0:
            num_divisors += 1
            if num / i != i:
                num_divisors += 1
    return num_divisors

def get_triangle_number(more_than_many_divisors: int) -> int:
    for triangle_num in generate_triangle_number():
        if count_divisors(triangle_num) > more_than_many_divisors:
            return triangle_num
    assert False, "Unreachable"

if __name__ == '__main__':
    print(get_triangle_number(500))