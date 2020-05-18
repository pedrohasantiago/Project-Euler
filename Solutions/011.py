# In the 20×20 grid below, four numbers along a diagonal line have been
# marked in red.

# 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
# 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
# 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
# 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
# 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
# 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
# 32 98 81 28 64 23 67 10 **26** 38 40 67 59 54 70 66 18 38 64 70
# 67 26 20 68 02 62 12 20 95 **63** 94 39 63 08 40 91 66 49 94 21
# 24 55 58 05 66 73 99 26 97 17 **78** 78 96 83 14 88 34 89 63 72
# 21 36 23 09 75 00 76 44 20 45 35 **14** 00 61 33 97 34 31 33 95
# 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
# 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
# 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
# 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
# 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
# 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
# 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
# 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
# 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
# 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same
# direction (up, down, left, right, or diagonally) in the 20×20 grid?
# (Link: https://projecteuler.net/problem=11.)

from math import prod
from functools import partial
from itertools import islice

def greatest_product_of_adjacent_digits(stream, digits_in_num,
                                        adjacent_numbers):
    """Return the highest product of "adjacent_numbers" adjacent (either up, down,
    left, right, or diagonally) integers in a sliceable "stream" (a string of numbers
    with lines delimited by newlines; the number of lines and numbers in each line should be the same).
    """
    def get_grid_size(stream, digits_in_num):
        digits_in_line = len(stream.split('\n')[0])
        return digits_in_line // digits_in_num

    def highest_product_in_selection(selection, adjacent_numbers):
        init = 0
        highest_product = float('-inf')
        while (slice_ := init + adjacent_numbers) <= len(selection):
            current_product = prod(x for x in selection[init:slice_])
            highest_product = max(highest_product, current_product)
            init += 1
        return highest_product

    def traverse_horizontally(stream):
        """Traverse the stream horizontally (left or right). Adaptation
        of Problem 8.
        """
        highest_product = float("-inf")
        for line in stream:
            current_product = highest_product_in_selection(line, adjacent_numbers)
            highest_product = max(highest_product, current_product)
        return highest_product

    def traverse_vertically(stream):
        """Traverse the stream vertically (up or down)."""
        highest_product = float("-inf")
        for column in range(GRID_SIZE):
            selection = [row[column] for row in stream]
            current_product = highest_product_in_selection(selection, 
                                                          adjacent_numbers)
            highest_product = max(highest_product, current_product)
        return highest_product

    def traverse_diagonally(stream):
        """Traverse the stream diagonally (both ascending and
        descending).
        """
        def traverse_diagonally_given_direction(stream, descending, max_val):
            minuend = 0 if descending is True else GRID_SIZE - 1
            highest_product = float("-inf")
            for init in range(GRID_SIZE):
                if (init <= max_val) and (GRID_SIZE - init >= adjacent_numbers):
                    selection = []
                    for i, line in zip(range(init, init + GRID_SIZE), stream):
                        if (descending and minuend - i <= 0
                            or not descending and minuend - i >=0):
                            try:
                                selection.append(line[abs(minuend - i)])
                            except IndexError:
                                break
                    highest_product = max(
                        highest_product,
                        highest_product_in_selection(selection,
                                                     adjacent_numbers)
                    )
            return highest_product
        
        highest_product = float('-inf')
        for i in range(GRID_SIZE):
            max_val = 0 if i != 0 else float('inf')
            sliced_stream = list(islice(stream, i, None))
            traverse_stream = partial(traverse_diagonally_given_direction,
                                      stream=sliced_stream, max_val=max_val)
            highest_product = max(traverse_stream(descending=True),
                                  traverse_stream(descending=False))
        return highest_product
        

    # Parsing the stream into an iterable of iterables
    # First, by creating an iterable of "digits_in_num"-digit numbers.
    # Finally, by splitting the iterable into as many lines as given by
    # "GRID_SIZE":
    GRID_SIZE = get_grid_size(stream, digits_in_num)
    stream_no_breaks = stream.replace('\n', '')
    stream_agg_ints = [int(stream_no_breaks[i:i + digits_in_num])
                       for i in range(0, len(stream_no_breaks), digits_in_num)]
    stream_split_into_lines = [stream_agg_ints[i:i + GRID_SIZE]
                               for i in range(0, len(stream_agg_ints), GRID_SIZE)]

    return max(func(stream_split_into_lines)
               for func in (traverse_horizontally,
                            traverse_vertically,
                            traverse_diagonally))

if __name__ == "__main__":
    stream = ("0802229738150040007504050778521250779108\n"
              "4949994017811857608717409843694804566200\n"
              "8149317355791429937140675388300349133665\n"
              "5270952304601142692468560132567137023691\n"
              "2231167151676389419236542240402866331380\n"
              "2447326099034502447533537836842035171250\n"
              "3298812864236710263840675954706618386470\n"
              "6726206802621220956394396308409166499421\n"
              "2455580566739926971778789683148834896372\n"
              "2136230975007644204535140061339734313395\n"
              "7817532822753167159403800462161409535692\n"
              "1639054296353147555888240017542436298557\n"
              "8656004835718907054444374460215851541758\n"
              "1980816805944769287392138652177704895540\n"
              "0452088397359916079757321626267933279866\n"
              "8836688757622072034633674655123263935369\n"
              "0442167338253911249472180846293240627636\n"
              "2069364172302388346299698267598574043616\n"
              "2073352978319001743149714886811623570554\n"
              "0170547183515469169233486143520189196748\n")
    print(greatest_product_of_adjacent_digits(stream, 2, 4))