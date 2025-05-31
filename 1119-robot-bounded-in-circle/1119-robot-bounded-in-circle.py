class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 4 directions: North, East, South, West (clockwise order)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Starting position (0, 0), facing North (index 0)
        x = y = 0
        dir_idx = 0

        for ch in instructions:
            if ch == 'G':
                dx, dy = directions[dir_idx]
                x += dx
                y += dy
            elif ch == 'L':
                # 90° left => previous direction (anticlockwise)
                dir_idx = (dir_idx + 3) % 4
            elif ch == 'R':
                # 90° right => next direction (clockwise)
                dir_idx = (dir_idx + 1) % 4

        # 2 conditions jisme robot bounded hoga:
        # 1. Wapas (0,0) pe aa gaya ho
        # 2. Direction change ho gaya ho (matlab ghoom ke circle banega)
        return (x == 0 and y == 0) or dir_idx != 0

        