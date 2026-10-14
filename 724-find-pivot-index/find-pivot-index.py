class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        l = 0
        r = sum(nums[1:])
        if l == r:
            return 0
        for i in range(0, len(nums)-1):
            l += nums[i]
            r -= nums[i+1]
            if l == r:
                return i+1
                break
        else:
            return -1