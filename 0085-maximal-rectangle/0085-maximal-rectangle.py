class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # edge case 不要忘记！
        if not matrix:
           return 0
        histogram = [0] * (len(matrix[0]) + 1)
        maxSize = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                histogram[j] = histogram[j] + 1 if matrix[i][j] == "1" else 0
            maxSize = max(maxSize, self.get_largest_from_histogram(histogram))
        return maxSize
    
    def get_largest_from_histogram(self, array):
        stack = []
        max_area = 0
        for i in range(len(array)):
            while stack and array[stack[-1]] > array[i]:
                top_index = stack.pop()
                max_area = max(max_area, array[top_index] * ((i - stack[-1] - 1) if stack else i))

            stack.append(i)
        return max_area