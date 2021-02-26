# Lists can be used to represent mathematical vectors.
# In this exercise and several that follow you will write functions to perform standard operations on vectors.
# Create a file named vectors.py and write Python code to make the doctests for each function pass.
#
# Write a function add_vectors(u, v) that takes two lists of numbers of the same length,
# and returns a new list containing the sums of the corresponding elements of each.

def add_vectors(u, v):
    """
          >>> add_vectors([1, 0], [1, 1])
          [2, 1]
          >>> add_vectors([1, 2], [1, 4])
          [2, 6]
          >>> add_vectors([1, 2, 1], [1, 4, 3])
          [2, 6, 4]
          >>> add_vectors([11, 0, -4, 5], [2, -4, 17, 0])
          [13, -4, 13, 5]
          >>> a = [1, 2, 3]
          >>> b = [1, 1, 1]
          >>> add_vectors(a, b)
          [2, 3, 4]
          >>> a
          [1, 2, 3]
          >>> b
          [1, 1, 1]
        """

    final =[]
    for i in range(0,len(v)):
        final.append(u[i]+v[i])
    return final

# python -m doctest -v  vector_001.py

