class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, code in enumerate(s.encode('ascii'), 1):
            total_sum += (123 - code) * i
        return total_sum