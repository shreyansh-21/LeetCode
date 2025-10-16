class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<=0:
            neg = True
        a = str(abs(x))
        x= int(a[::-1])
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0

        return x* -1 if neg else x
        