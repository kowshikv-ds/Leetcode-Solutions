class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k
        for num in nums:
            new_dp = [0] * k
            num_mod = num % k
            new_dp[num_mod] += 1
            for r in range(k):
                if dp[r] > 0:
                    new_mod = (r * num_mod) % k
                    new_dp[new_mod] += dp[r]
            for x in range(k):
                result[x] += new_dp[x]
            dp = new_dp
        return result