"""Get triangle number with more than a certain number of divisors."""
# What is the value of the first triangle number to have over five
# hundred divisors?
# (Link: https://projecteuler.net/problem=12)

from math import sqrt
from typing import Iterable, List

def _triangle_number_iterator() -> Iterable[int]:
    curr = 2
    while True:
        yield sum(range(curr))
        curr += 1

def _sieve_of_erastothenes(limit: int) -> Iterable[int]:
    # Taken from https://stackoverflow.com/a/3941967/12058106
    # Initialize list with highest index = limit
    is_index_prime: List[bool] = ([False] * 2) + ([True] * (limit - 1))
    is_index_prime[0] = is_index_prime[1] = False # 0 and 1 arent primes
    # Iterate on list; return if prime
    for i, is_prime in enumerate(is_index_prime):
        if is_prime:
            yield i
            # Cut off non-primes
            if i == 2:
                step = i
            else:
                step = 2*i # No need to iterate on even numbers again
            for not_prime in range(i * i, limit, step):
                is_index_prime[not_prime] = False

def _divisor_function(num: int) -> int:
    # Inspired by https://www.geeksforgeeks.org/count-divisors-n-on13/
    divisors = 1 # All numbers have at least 1 divisor (1)
    for prime in _sieve_of_erastothenes(limit=num):
        # Is divisor?
        if num % prime == 0:
            # If divisor, what is the highest power to get to num?
            power = 0
            while num % prime == 0:
                num = int(num / prime)
                power += 1
            # If n = 1**u_1 * 2**u_2 * 3**u_3 ... p**u_r,
            # The number of divisors is
            # (1 + u_1)(1 + u_2)(1 + u_3)...(1 + u_r) 
            divisors *= power + 1
    return divisors

def get_triangle_number(more_than_many_divisors: int) -> int:
    for triangle_num in _triangle_number_iterator():
        if _divisor_function(triangle_num) > more_than_many_divisors:
            return triangle_num
    assert False, "Unreachable"

if __name__ == '__main__':
    print(get_triangle_number(500))