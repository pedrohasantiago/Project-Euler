# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder. What is the smallest positive
# number that is evenly divisible (divisible with no remainder) by all
# of the numbers from 1 to 20?
# (Link: https://projecteuler.net/problem=5.)

def smallest_evenly_divisible(min_divisor, max_divisor, minimum_dividend=0):
    """Returns the smallest number that is evenly divisible (divisible
    with no remainder) by all of the numbers from `min_divisor` to
    `max_divisor`. If a `minimum_dividend` is provided, only dividends
    greater than this number will be evaluated.
    """
    factors = range(max_divisor,0,-min_divisor)
    while True:
        counter = 0
        for i in factors:
            if minimum_dividend % i != 0:
                break
            else:
                counter += 1
        if counter == len(factors):
            return minimum_dividend 
        minimum_dividend += 1

if __name__ == "__main__":
    print(smallest_evenly_divisible(1, 20, 2520))