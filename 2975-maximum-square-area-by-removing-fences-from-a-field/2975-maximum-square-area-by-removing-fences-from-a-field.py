class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: list[int], vFences: list[int]) -> int:
        
        h = sorted([1] + hFences + [m])
        v = sorted([1] + vFences + [n])
        
        #collect all distances for horizontal
        H = set()
        for i in range(len(h)):
            for j in range(i + 1, len(h)):
                H.add(h[j] - h[i])
        
        #collect all distances for vertical
        V = set()
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                V.add(v[j] - v[i])
        
        #find common distances
        common = H & V
        
        if not common:
            return -1
        
        side = max(common)
        MOD = 1_000_000_007
        return (side * side) % MOD

