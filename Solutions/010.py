# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
# (Link: https://projecteuler.net/problem=10.)

from math import sqrt

def sum_of_primes_below(threshold):
    """Return the sum of all prime numbers below a given threshold."""
    # Using the same function from Problem 7:
    def is_prime(j):
        """Return `True` if `j` is prime; `False` if not."""
        # Loop through all numbers smaller than `j` and bigger than 1 to
        # check if there is any divisor. Note that it is only necessary
        # to loop through numbers smaller than the sqrt of `j`.
        for i in range(int(sqrt(j)), 1, -1):
            # If there is any divisor, `j` is not prime: 
            if j % i == 0:
                return False
        # Otherwise, `j` is prime:
        return True

    return sum(i for i in range(2, threshold+1) if is_prime(i) == True)

if __name__ == "__main__":
    print(sum_of_primes_below(2000000))