class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ""
        k = sum // 9
        r = sum % 9
        if r > 0:
            return "9" * k + str(r) + "0" * (num - k - 1)
        else:
            return "9" * k + "0" * (num - k)