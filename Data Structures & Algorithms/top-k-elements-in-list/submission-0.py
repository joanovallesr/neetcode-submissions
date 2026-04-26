class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for n, f in freq.items():
            buckets[f].append(n)

        res = []

        for f in range(len(nums), 0 , -1):
            for n in buckets[f]:
                res.append(n)
                if len(res) == k:
                    return res
        
        return res