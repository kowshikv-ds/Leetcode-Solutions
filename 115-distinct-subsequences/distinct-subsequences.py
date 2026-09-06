class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len_s, len_t = len(s), len(t)
        if len_s < len_t:
            return 0
        t_indices = defaultdict(list)
        for idx, char in enumerate(t):
            t_indices[char].append(idx)
        for char in t_indices:
            t_indices[char].reverse()
        dp = [0] * (len_t + 1)
        dp[0] = 1
        for char_s in s:
            if char_s in t_indices:
                for j in t_indices[char_s]:
                    dp[j + 1] += dp[j]
        return dp[len_t]