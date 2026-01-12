class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            # dx = |x2 - x1|
            # dy = |y2 - y1|
            # So the minimum time to move between two points is simply:max(|x2 - x1|, |y2 - y1|)
            ans += max(
                abs(points[i][0] - points[i - 1][0]),
                abs(points[i][1] - points[i - 1][1])
            )
        return ans
            
