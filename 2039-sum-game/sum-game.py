class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2
        cnt = 0
        total = 0
        for i in num[:mid]:
            if i.isdigit():
                total += int(i)
            else:
                cnt += 1
        for i in num[mid:]:
            if i.isdigit():
                total -= int(i)
            else:
                cnt -= 1
        return not (2 * total == -9 * cnt)