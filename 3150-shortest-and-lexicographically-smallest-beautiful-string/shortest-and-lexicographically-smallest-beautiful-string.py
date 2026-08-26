class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        window = k
        right = k
        ans = ''
        n = len(s)
        while right <= n:
            left = 0
            for i in range(n - right + 1):
                sstr = s[left:right]
                cnt = sstr.count('1')
                if cnt == k:
                    if ans == '':
                        ans = sstr
                    elif sstr < ans:
                        ans = sstr
                left += 1
                right += 1
            if ans != '':
                break
            else:
                window += 1
                right = window
        return ans