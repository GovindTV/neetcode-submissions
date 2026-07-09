class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxl, maxr = 0,0
        res = 0
        while l < r:
            maxl = max(height[l], maxl)
            maxr = max(height[r], maxr)

            if maxl < maxr:
                res += maxl - height[l]
                l += 1
            else:
                res += maxr - height[r]
                r -= 1
        return res