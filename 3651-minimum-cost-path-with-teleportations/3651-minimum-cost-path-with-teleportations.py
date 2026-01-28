class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        line = sorted(((grid[i][j], i, j) for i in range(m) for j in range(n)), key = lambda v: -v[0])
        line.append((-1, 0, 0))

        dp = [[inf] * (n+1) for _ in range(m+1)]
        dp[0][1] = 0 
       
        for i, j in product(range(m), range(n)):
            dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1]) + (grid[i][j] if i or j else 0)

        for _ in range(k):
            curr_min, teleport = inf, {}
            for i in range(len(line)):
                if line[i-1][0] != line[i][0]:
                    teleport[line[i-1][0]] = curr_min
                curr_min = min(dp[line[i][1]+1][line[i][2]+1], curr_min)
            for i, j in product(range(m), range(n)):
                dp[i+1][j+1] = min(dp[i+1][j] + grid[i][j], dp[i][j+1] + grid[i][j], teleport[grid[i][j]])
        return dp[-1][-1]