class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        res = []
        for _ in range(k):
            _, val = heapq.heappop(heap)
            res.append(val)
        return res


