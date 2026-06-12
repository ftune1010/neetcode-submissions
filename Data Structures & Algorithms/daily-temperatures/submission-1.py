class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res, stack = [0] * n, []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, day = stack.pop()
                res[day] = i - day
            stack.append((temp, i))
        return res