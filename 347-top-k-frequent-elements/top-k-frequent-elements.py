class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occur = {}
        for num in nums:
            occur[num] = occur.get(num, 0) + 1

        count = [[] for _ in range(len(nums) + 1)]
        res = []

        for key in occur:
            count[occur[key]].append(key)

        for bucket in reversed(count):
            for key in bucket:
                res.append(key)
                if len(res) == k:
                    return res
        return res
