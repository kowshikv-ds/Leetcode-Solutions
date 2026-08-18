class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == n:
            return max(nums)
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
        ans = -1
        if k == 1:
            for key, val in freq.items():
                if val == 1:
                    ans = max(ans, key)
            return ans
        if freq[nums[0]] == 1:
            ans = max(ans, nums[0])
        if freq[nums[-1]] == 1:
            ans = max(ans, nums[-1])
        return ans