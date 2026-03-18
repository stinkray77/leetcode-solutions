class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num1 in enumerate(nums):
            complement = target - num1
            if complement in seen:
                return [seen[complement], i]
            seen[num1] = i

        return []
