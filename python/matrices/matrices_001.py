# Create a new module named matrices.py and
# add the following function,
# which returns a copy of nested lists of numbers such that the lists are not aliases:
import copy
def copy_matrix(matrix):
    """
      >>> copy_matrix([[1, 2], [3, 4]])
      [[1, 2], [3, 4]]
      >>> copy_matrix([[1, 2, 3], [4, 5, 6]])
      [[1, 2, 3], [4, 5, 6]]
      >>> copy_matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
      [[1, 2], [3, 4], [5, 6], [7, 8]]
      >>> m = [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
      >>> copyofm = copy_matrix(m)
      >>> copyofm
      [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
      >>> for row_num, row in enumerate(copyofm):
      ...     for col_num, col_val in enumerate(row):
      ...         copyofm[row_num][col_num] = 42
      ...
      >>> copyofm
      [[42, 42, 42], [42, 42, 42], [42, 42, 42]]
      >>> m
      [[1, 0, 0], [0, 2, 0], [0, 0, 3]]
    """
    x = copy.deepcopy(matrix)
    return x

