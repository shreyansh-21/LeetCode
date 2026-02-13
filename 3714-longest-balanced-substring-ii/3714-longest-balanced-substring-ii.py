class Solution:
    def longestBalanced(self, s: str) -> int:
        ca = 0
        cb = 0
        cc = 0
        ans = 0
        
        cur = 0
        prev = ''
        
        h_all = {(0, 0): -1}
        h1 = {(0, 0): -1}
        h2 = {(0, 0): -1}
        h3 = {(0, 0): -1}
        
        for i in range(len(s)):
            if s[i] == 'a':
                ca += 1
            elif s[i] == 'b':
                cb += 1
            else:
                cc += 1
            
            if s[i] == prev:
                cur += 1
            else:
                cur = 1
                prev = s[i]
            ans = max(ans, cur)
            
            d1 = ca - cb
            d2 = cb - cc
            d3 = ca - cc
            
            k_all = (d1, d3)
            k1 = (d1, cc)
            k2 = (d2, ca)
            k3 = (d3, cb)
            
            if k_all in h_all:
                ans = max(ans, i - h_all[k_all])
            else:
                h_all[k_all] = i
            
            if k1 in h1:
                ans = max(ans, i - h1[k1])
            else:
                h1[k1] = i
            
            if k2 in h2:
                ans = max(ans, i - h2[k2])
            else:
                h2[k2] = i
            
            if k3 in h3:
                ans = max(ans, i - h3[k3])
            else:
                h3[k3] = i
        
        return ans