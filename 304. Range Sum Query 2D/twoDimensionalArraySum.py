from typing import List

# 304. Range Sum Query 2D - Immutable (https://leetcode.com/problems/range-sum-query-2d-immutable/)

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.prefixSum = [[0]*(col+1) for i in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                self.prefixSum[i][j] = matrix[i-1][j-1] + self.prefixSum[i-1][j] + self.prefixSum[i][j-1] - self.prefixSum[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Some weird prefix sum thing I looked up...
        return self.prefixSum[row2+1][col2+1] - self.prefixSum[row1][col2+1] - self.prefixSum[row2+1][col1] + self.prefixSum[row1][col1]

        # # Iterative approach too slow for large data sets
        # total = 0
        # for row in range(row2 - row1 + 1):
        #     for column in range(col2 - col1 + 1):
        #         sum += self.matrix[row + row1][column + col1]
        # return total