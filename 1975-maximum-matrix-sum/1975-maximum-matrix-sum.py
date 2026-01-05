class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negCount = 0
        minNum = float("inf")
        for i in matrix:
            for j in i:
                total = total + abs(j)
                if j < 0:
                    negCount += 1
                    minNum = min(minNum, abs(j))

        if negCount % 2 == 0:
            return total
        else:
            return total - 2 * minNum
