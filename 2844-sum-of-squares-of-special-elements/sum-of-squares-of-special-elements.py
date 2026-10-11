class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for i in range(n):
            position = i + 1
            if n % position == 0:
                total_sum += nums[i] ** 2
        return total_sum