class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 30
        for num in nums:
            for i in range(30):
                if (num >> i) & 1:
                    bit_counts[i] += 1
        total_sum_of_squares = 0
        for _ in range(k):
            current_num = 0
            for i in range(30):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            total_sum_of_squares = (total_sum_of_squares + current_num * current_num) % MOD
        return total_sum_of_squares