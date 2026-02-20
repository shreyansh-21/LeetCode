class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        start,count = 0,0
        res = []
        
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            else:
                count -= 1
            
            if count == 0:
                # recursively solve 
                inner = self.makeLargestSpecial(s[start + 1:i])
                res.append('1' + inner + '0')
                start = i + 1

        res.sort(reverse=True)
        return ''.join(res)