def sum_even_fibonacci_terms(limit):
    """Returns the sum of even fibonacci numbers below a given limit.
    """
    # Initializing the Fibonacci sequence:
    second_to_last_term = 1
    last_term = 1
    sum = 0
    # Appending numbers below the limit:
    while last_term < limit:
        new_term = last_term + second_to_last_term
        second_to_last_term = last_term
        last_term = new_term
        # Summing even numbers:
        if new_term % 2 == 0:
            sum += new_term
    return sum
