# Write a function add_matrices(m1, m2) that adds m1 and m2 and returns a new matrix containing their sum.
# You can assume that m1 and m2 are the same size.
# You add two matrices by adding their corresponding values.
import copy
def add_matrices(m1, m2):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> b = [[2, 2], [2, 2]]
      >>> add_matrices(a, b)
      [[3, 4], [5, 6]]
      >>> c = [[8, 2], [3, 4], [5, 7]]
      >>> d = [[3, 2], [9, 2], [10, 12]]
      >>> add_matrices(c, d)
      [[11, 4], [12, 6], [15, 19]]
      >>> c
      [[8, 2], [3, 4], [5, 7]]
      >>> d
      [[3, 2], [9, 2], [10, 12]]
   """
    c=[]


    for i in range(0,len(m1)):
        temp = []
        for j in range(0,2):
            temp.append(m1[i][j]+m2[i][j])
        c.append(temp)
    return c



a = [[1, 2], [3, 4]]
b = [[2, 2], [2, 2]]
print(add_matrices(a, b))
# [[3, 4], [5, 6]]