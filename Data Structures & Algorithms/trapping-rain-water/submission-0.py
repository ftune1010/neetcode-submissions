class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_wall = [0] * n
        right_wall = [0] * n

        for i in range(1, n):
            left_wall[i] = max(left_wall[i - 1], height[i - 1])
        for i in range(n - 2, -1, -1):
            right_wall[i] = max(right_wall[i + 1], height[i + 1])
        
        print(f"{left_wall = }")
        print(f"{right_wall = }")
        water = 0
        for i in range(n):
            min_wall = min(left_wall[i], right_wall[i])
            water += max(0, min_wall - height[i])
        return water