from math import sqrt

def highest_prime_factor(num):
    """Returns the highest prime divisor (factor) of any number.
    """
    def factors_when_not_cousin(n):
        """Returns all the divisors (factors) of a number, except those
        specific of a cousin number, ie, 1 and itself.
        """
        factors = []
        # Looping through all numbers smaller than `n` to check which
        # are its divisors. Please note that is is only necessary to
        # loop through numbers smaller than the sqrt of `n`.
        for i in range(int(sqrt(n)), 1, -1):
            if n % i == 0:
                factors.append(i)
                factors.append(int(n/i))
        return set(factors)
    factors = factors_when_not_cousin(num)
    # If num is a cousin number, it itself will be the highest factor:
    if not factors:
        return num
    else:
        # We will go down a factor tree until only prime factors are
        # left.
        counter = 0
        while True:
            factors = list(set(factors))
            # Case when there are only prime factors remaining:
            if counter == len(factors):
                break
            loopable_factors = set(factors) # There is no need to loop
                                            # thorugh repeating factors.
            counter = 0
            for i in loopable_factors:
                new_factors = factors_when_not_cousin(i)
                if not new_factors: # If the new found factor is cousin,
                    counter += 1 # ...add 1 for each prime factor.
                    continue
                factors.remove(i) # We shouldn't loop through numbers
                                  # whose factors were already found.
                factors += new_factors # We should loop through the new
                                       # found factors.
    return max(factors)