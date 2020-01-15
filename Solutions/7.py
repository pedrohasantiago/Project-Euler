# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13. What is the 10 001st prime number?
# (Link: https://projecteuler.net/problem=7.)

from math import sqrt

def nth_prime(n):
    """Returns the n-th prime number, considering that the first prime
    number is 1.
    """

    def is_prime(j):
        """Returns `True` if `j` is prime; `False` if not.
        """
        # Loop through all numbers smaller than `j` and bigger than 1 to
        # check if there is any divisor. Note that is is only necessary to
        # loop through numbers smaller than the sqrt of `j`.
        for i in range(int(sqrt(j)), 1, -1):
            # If there is any divisor, `j` is not prime: 
            if j % i == 0:
                return False
        # Otherwise, `j` is prime:
        return True

    counter = 1
    prime = 2 # This is the counter-th prime.
    while counter < n:
        while True:
            prime += 1
            if is_prime(prime):
                counter += 1
                break
    return prime

if __name__ == "__main__":
    print(nth_prime(10001))