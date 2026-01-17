class Solution:
    def largestSquareArea(self, bottomLeft, topRight):
        n = len(bottomLeft)
        max_side = 0

        for i in range(n):
            x1a, y1a = bottomLeft[i]
            x2a, y2a = topRight[i]
            for j in range(i + 1, n):
                x1b, y1b = bottomLeft[j]
                x2b, y2b = topRight[j]

                # overlapping rectangle
                ix1 = max(x1a, x1b)
                iy1 = max(y1a, y1b)
                ix2 = min(x2a, x2b)
                iy2 = min(y2a, y2b)

                # width and height of overlap
                w = ix2 - ix1
                h = iy2 - iy1

                # only consider positive overlap
                if w > 0 and h > 0:
                    side = min(w, h)
                    max_side = max(max_side, side)

        return max_side * max_side
