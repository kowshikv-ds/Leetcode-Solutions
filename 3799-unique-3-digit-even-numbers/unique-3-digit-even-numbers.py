class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        counts = Counter(digits)
        ans = 0
        for num in range(100, 1000, 2):
            s = str(num)
            sc = Counter([int(c) for c in s])
            possible = True
            for k, v in sc.items():
                if counts[k] < v:
                    possible = False
                    break
            if possible:
                ans += 1
        return ans