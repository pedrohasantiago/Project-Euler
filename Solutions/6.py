# The sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)**2 = 55**2 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 − 385 = 2640. Find
# the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.
# (Link: https://projecteuler.net/problem=6.)

def difference_sum_of_squares_square_of_sums(min, max):
    """Find the difference between (i) the sum of the squares of the
    numbers in a range and (ii) the square of the sum of the numbers in
    the same range. The `min` and `max` parameters define the minimum
    and maximum integers that make up the range in question.
    """
    target = range(min, max+1)
    return sum(target)**2 - sum((i**2 for i in target))

if __name__ == "__main__":
    print(difference_sum_of_squares_square_of_sums(0, 100))