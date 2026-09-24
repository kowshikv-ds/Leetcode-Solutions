class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == sum(int(_) for _ in str(n)):
                return i
        else:
            return -1