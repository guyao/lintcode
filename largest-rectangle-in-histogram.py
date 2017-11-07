# http://lintcode.com/en/problem/largest-rectangle-in-histogram/


class Solution(object):
    """
    @param: height: A list of integer
    @return: The area of largest rectangle in the histogram
    """

    def largestRectangleArea(self, height):
        if not height:
            return 0
        INF = float('inf')
        s = []
        mx = -INF
        hs = height + [-INF]
        for i, n in enumerate(hs):
            cur = n
            while s and cur <= height[s[-1]]:
                h = height[s.pop()]
                w = i - s[-1] - 1 if s else i
                mx = max(mx, h * w)
            s.append(i)
        return mx


t = [2, 1, 5, 6, 2, 3] # expect 10
r = Solution().largestRectangleArea(t)
print(r)
