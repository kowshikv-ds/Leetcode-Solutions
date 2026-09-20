class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i, char in enumerate(s):
            pos = 26 - (ord(char) - ord('a'))
            ans += pos * (i+1)
        return ans