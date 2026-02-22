class Solution:
    def binaryGap(self, n: int) -> int:
        b=bin(n)[2:]
        if b.count('1')<=1:
            return 0
        c=0
        m=0
        for i in b:
            if i=='0':
                c+=1
            elif i=='1':
                m=max(m,c+1)
                c=0
        return m
        