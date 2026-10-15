class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        l = 0
        r = 1
        n = len(nums)
        ans = 0
        for i in range((n*(n+1))//2):
            ans += len(set(nums[l:r])) ** 2
            if r == n:
                l += 1
                r = l + 1
            else:
                r += 1
        return ans