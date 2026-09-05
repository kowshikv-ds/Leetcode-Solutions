class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suff_min = [0] * n
        curr_min = nums[-1]
        for i in range(n - 1, -1, -1):
            if nums[i] < curr_min:
                curr_min = nums[i]
            suff_min[i] = curr_min
        pref_max = nums[0]
        for i in range(n):
            if nums[i] > pref_max:
                pref_max = nums[i]
            if pref_max - suff_min[i] <= k:
                return i
        return -1