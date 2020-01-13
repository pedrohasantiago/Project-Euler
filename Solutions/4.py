# A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 × 99. Find
# the largest palindrome made from the product of two 3-digit numbers.
# (Link: https://projecteuler.net/problem=4.)

def highest_palindrome_product(digits):
    """Returns the highest palindrome number resulting from the
    multiplication of two numbers with the given amount of digits.
    """
    def is_palindrome(target):
        """Returns True if target (str or int) is a palindrome.
        """
        string = str(target)
        return list(string) == list(string)[::-1]
    # Creating the two highest possible numbers with the given amount of
    # digits:
    highest_number1 = highest_number2 = int("9"*digits)
    palindromes_list = []
    while True:
        result = highest_number1 * highest_number2
        if is_palindrome(result):
            palindromes_list.append(result)
        # Finding the products between all two numbers with the given
        # amount of digits:
        if highest_number2 == int("1" + "0"*(digits-1)):
            if highest_number1 == int("1" + "0"*(digits-1)):
                break
            else:
                highest_number2 = highest_number1
                highest_number1 -=1
        else:
            highest_number2 -= 1
    return max(palindromes_list)

if __name__ == "__main__":
    print(highest_palindrome_product(3))