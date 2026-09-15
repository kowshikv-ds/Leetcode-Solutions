class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        def is_palindrome(l: int, r: int) -> bool:
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        for i in range(n):
            dp[i + 1] = dp[i]
            if i + 1 >= k and is_palindrome(i - k + 1, i):
                dp[i + 1] = max(dp[i + 1], dp[i - k + 1] + 1)
            if i + 1 >= k + 1 and is_palindrome(i - k, i):
                dp[i + 1] = max(dp[i + 1], dp[i - k] + 1)
        return dp[n]