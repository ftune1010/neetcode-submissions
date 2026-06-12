class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        heap = []
        l = 0
        for r in range(len(nums)):
            if r < k - 1:
                heapq.heappush_max(heap, (nums[r], r))
                continue
            heapq.heappush_max(heap, (nums[r], r))
            while heap[0][1] < l:
                heapq.heappop_max(heap)
            res.append(heap[0][0])
            l += 1

        return res