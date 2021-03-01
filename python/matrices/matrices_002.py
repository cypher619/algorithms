# Then add each of the following functions to the matrices.py module, one at a time,
# making sure the doctests pass for each one before adding the next.
import copy


def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    mat = copy.deepcopy(matrix)
    temp = []
    for i in range(0, len(mat[-1])):
        temp.append(0)
    mat.append(temp)
    return mat




def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    mat = copy.deepcopy(matrix)
    for i in mat:
        i.append(0)
    return mat
