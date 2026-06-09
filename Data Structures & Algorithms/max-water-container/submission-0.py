class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r - l) * min(heights[r], heights[l]))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return ans