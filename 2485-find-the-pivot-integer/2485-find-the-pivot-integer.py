class Solution:
    def pivotInteger(self, n: int) -> int:
        totalsum = n*(n+1)//2
        currsum = 0
        for i in range(1,n+1):
            currsum += i
            if currsum == totalsum -currsum+i:
                return i
        return -1

        