# If we list all the natural numbers below 10 that are multiples of 3 or
# 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the
# sum of all the multiples of 3 or 5 below 1000.
# (Link: https://projecteuler.net/problem=1.)

def sum_multiples_3_and_5(number):
    """Returns the sum of all multiples of 3 and 5 below a given number.
    """
    # The first possible integer multiple of 3 and 5 is 3:
    counter = 3
    # Multiples of 3 and 5 start at 3 and increase according to a pattern:
    pattern = (i for i in [2, 1, 3, 1, 2, 3, 3])
    sum = 0
    while counter < number:
        sum += counter
        try:
            counter += next(pattern)
        except StopIteration:
            pattern = (i for i in [2, 1, 3, 1, 2, 3, 3])
            counter += next(pattern)
    return sum

print(sum_multiples_3_and_5(1000))