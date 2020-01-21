# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which, a**2 + b**2 = c**2. For example,
# 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which
# a + b + c = 1000.
# Find the product abc.
# (Link: https://projecteuler.net/problem=9.)

from math import sqrt

def find_pythagorian_triplet(abc_sum, only_natural=False):
    """Return a list of pythagorian triplets whose sum is abc_sum. When
    "abc_sum" is not an integer, a maximum of 2 triplets is provided.
    If "only_natural" is True, only pythagorian triplets wholly composed
    of natural numbers will be returned. In this case the list is
    exhaustive - otherwise, it is not.
    """
    # Considering Euclid's formula, a pythagorian triplet can be
    # decomposed into any "m" and "n" such that:

    # a = 2*m*n
    # b = m**2 - n**2
    # c = m**2 + n**2

    # Replacing the definitions above for a, b and c in "a + b + c =
    # abc_sum", it follows that "m*(m + n) = (abc_sum/2)" (1).

    # If we consider that a, b and c are natural numbers, m and n should
    # be integers (otherwise, there are infinite solutions). This means
    # that, in (1), "m" and "(m+n)" are such as the multiplication of
    # the factors of "abc_sum/2".

    # To solve (1) for its integer roots, we should find the factors of
    # "abc_sum/2". We can adapt one function used in Problem #3 in which
    # we loop through all numbers smaller than "abc_sum/2" to check
    # which are its divisors. It is only necessary to loop through
    # numbers smaller than the sqrt of "abc_sum/2".
    constant = abc_sum/2
    factors = [1, abs(constant)] + [i for i in range(int(sqrt(abs(constant))),
                                                     1, -1)
                                    if constant % i == 0]

    # We will replace these factors in (1) by creating a list with m and
    # n values taken from "m = factor" and "(m + n) = constant/factor".
    # Pairs with -m or -n are also possible; nevertheless, they make no
    # difference when calculating a, b and c.
    m_n_pairs = [(factor, (constant/factor)-factor) for factor in factors]

    # We will replace any m_n_pair in our definitions for a, b and c. If
    # we do not care about a, b and c being positive or not:
    triplets = [(2*m*n, m**2-n**2, m**2+n**2) for m, n in m_n_pairs]
    if only_natural == False:
        return triplets
    # Or, considering that a, b and c are all natural and, consequently,
    # all > 0. We do not have to check if c > 0, as "m**2 + n**2" is
    # always > 0 if m**2 - n**2 > 0.
    else:
        return list(filter(lambda triplet: triplet[0] > 0 and triplet[1] > 0,
                           triplets))

if __name__ == "__main__":
    from functools import reduce

    triplets = find_pythagorian_triplet(1000, only_natural=True)
    for triplet in triplets:
        print(reduce((lambda x, y: x*y), triplet))