"""Get triangle number with more than a certain number of divisors."""
# What is the value of the first triangle number to have over five
# hundred divisors?
# (Link: https://projecteuler.net/problem=12)

from math import sqrt
from typing import Iterable
import numpy as np

def _generate_triangle_number() -> Iterable[int]:
    curr = 1
    while True:
        # The n-th triangular number is the sum of all integers until n,
        # so it is basically a arithmetic projection of ratio 1:
        yield curr * (curr + 1) // 2
        curr += 1

def _sieve_of_erastothenes(limit: int) -> np.ndarray:
    # Taken from https://stackoverflow.com/a/3035188/12058106
    if limit < 2:
        return []
    limit += 1 # Including "limit" itself in the range
    # Initialize half sieve
    is_index_prime = np.ones(limit // 2, dtype=np.bool)
    # Iterate on sieve
    for i in range(3, int(sqrt(limit)) + 1, 2):
        if is_index_prime[i // 2]:
            # Cut off non-primes
            is_index_prime[i * i // 2 :: i] = False
    return np.insert(
        arr=2 * np.nonzero(is_index_prime)[0][1:] + 1,
        obj=0,
        values=2
    )

def _divisor_function(num: int) -> int:
    # Inspired by https://www.geeksforgeeks.org/count-divisors-n-on13/
    divisors = 1 # All numbers have at least 1 divisor (1)
    for prime in _sieve_of_erastothenes(limit=num):
        if prime > num:
            break
        # Is divisor?
        if num % prime == 0:
            # If divisor, what is the highest power to get to num?
            power = 0
            while num % prime == 0:
                num = num // prime
                power += 1
            # If n = 1**u_1 * 2**u_2 * 3**u_3 ... p**u_r,
            # The number of divisors is
            # (1 + u_1)(1 + u_2)(1 + u_3)...(1 + u_r) 
            divisors *= power + 1
    return divisors

def get_triangle_number(more_than_many_divisors: int) -> int:
    for triangle_num in _generate_triangle_number():
        if _divisor_function(triangle_num) > more_than_many_divisors:
            return triangle_num
    assert False, "Unreachable"

if __name__ == '__main__':
    print(get_triangle_number(500))