# Write a function scalar_mult(s, m) that multiplies a matrix, m, by a scalar, s.
import copy


def scalar_mult(s, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    final=[]
    for i in range(0,len(m)):
        temp=[]
        for j in range(0,len(m[0])):
            temp.append(m[i][j]*s)
        final.append(temp)


    return final

    # L = len(s[0])
    # final = []
    # for i in range(0,L):
    #     for j in range(0,len(m)):
    #         for k in range(0,len(s)):
    #             final[i][j] += s[i][k] * m[k][j]
    # return final

b = [[1, 2], [3, 4]]
print(scalar_mult(3, b))