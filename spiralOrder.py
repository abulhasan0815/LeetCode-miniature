# The function returns the elements of a 2D matrix in spiral order.
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:

            # Add first row/list of matrix
            ret += matrix.pop(0)

            # Append last element of all rows in order
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())

            # Add reverse of last row/list of matrix
            if matrix:
                ret += matrix.pop()[::-1]

            # Append first element of rows/ lists in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))

        return ret
