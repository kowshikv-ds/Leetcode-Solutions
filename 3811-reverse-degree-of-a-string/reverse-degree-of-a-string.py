class Solution:
    def reverseDegree(self, s: str) -> int:
        total_sum = 0
        for i, char_code in enumerate(s.encode('ascii'), 1):
            total_sum += (123 - char_code) * i
        return total_sum