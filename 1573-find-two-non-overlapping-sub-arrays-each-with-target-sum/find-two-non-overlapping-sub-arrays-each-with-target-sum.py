class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_map = {0: -1}
        current_sum = 0
        n = len(arr)
        dp = [float('inf')] * n
        min_total_len = float('inf')
        best_len_so_far = float('inf')
        for j, num in enumerate(arr):
            current_sum += num
            prefix_map[current_sum] = j
            needed_sum = current_sum - target
            if needed_sum in prefix_map:
                i = prefix_map[needed_sum]
                current_len = j - i
                best_len_so_far = min(best_len_so_far, current_len)
                if i >= 0 and dp[i] != float('inf'):
                    min_total_len = min(min_total_len, dp[i] + current_len)
            dp[j] = best_len_so_far
        return min_total_len if min_total_len != float('inf') else -1