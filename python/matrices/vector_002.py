# Write a function scalar_mult(s, v) that takes a number, s, and a list, v and returns the scalar multiple of v by s.

def scalar_mult(s, v):
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
      >>> a = [1, 2, 3]
      >>> scalar_mult(4, a)
      [4, 8, 12]
      >>> a
      [1, 2, 3]
    """
    w = v.copy()
    for i in range(0, len(w)):
        w[i] *= s

    return w
