# vis = [[False] * m] * n   ❌ wrong all list referece to same list 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        n = len(grid)
        m = len(grid[0])
        vist = [[False for _ in range(m)] for _ in range(n)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i,j,0))

        ans =0
        while queue:
            i,j,time = queue.popleft()
            ans = max(ans, time)
            # up
            if i - 1 >= 0 and not vist[i-1][j] and grid[i-1][j] == 1:
                queue.append((i-1, j, time + 1))
                vist[i-1][j] = True
            # down
            if i + 1 < n and not vist[i+1][j] and grid[i+1][j] == 1:
                queue.append((i+1, j, time + 1))
                vist[i+1][j] = True
            # left
            if j - 1 >= 0 and not vist[i][j-1] and grid[i][j-1] == 1:
                queue.append((i, j-1, time + 1))
                vist[i][j-1] = True
            # right
            if j + 1 < m and not vist[i][j+1] and grid[i][j+1] == 1:
                queue.append((i, j+1, time + 1))
                vist[i][j+1] = True

        # check if any fresh orange remains
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not vist[i][j]:
                    return -1

        return ans