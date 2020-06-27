# What is the value of the first triangle number to have over five
# hundred divisors?

from math import sqrt
from typing import Iterator

def triangle_number_iterator() -> Iterator[int]:
    curr = 2
    while True:
        yield sum(range(curr))
        curr += 1

def count_divisors(num: int) -> int:
    total = 0
    for i in range(1, int(sqrt(num)) + 1):
        if num % 1 == 0:
            if num / i == i:
                total += 1
            else:
                total += 2
    return total

def get_triangle_number(more_than_many_divisors: int) -> int:
    for triangle_num in triangle_number_iterator():
        if count_divisors(triangle_num) > more_than_many_divisors:
            return triangle_num
    assert False, "Unreachable"

if __name__ == '__main__':
    print(get_triangle_number(500))