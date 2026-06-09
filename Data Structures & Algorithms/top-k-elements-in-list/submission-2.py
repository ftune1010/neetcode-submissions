class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        
        count = Counter(nums)
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        for _ in range(k):
            _, key = heapq.heappop(heap)
            res.append(key)
        return res

       