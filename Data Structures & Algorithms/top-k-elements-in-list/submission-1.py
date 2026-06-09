class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        count = {}
        res = []
        for n in nums:
            count[n] = count.get(n, 0) + 1
        for key, val in count.items():
            bucket[val].append(key)
        for i in range(len(nums), 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res


