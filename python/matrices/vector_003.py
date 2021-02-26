# Write a function dot_product(u, v) that takes two lists of numbers of the same length,
# and returns the sum of the products of the corresponding elements of each (the dot_product).


def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    temp = 0
    for i in range(0, len(u)):
        temp += u[i] * v[i]

    return temp

