class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        sorted_intervals = sorted((ints[0], ints[1], ints[2], i) for i, ints in enumerate(intervals))
        left_bounds = [x[0] for x in sorted_intervals]
        n = len(intervals)
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            l, r, w, orig_idx = sorted_intervals[i]
            j = bisect.bisect_right(left_bounds, r)
            for k in range(1, 5):
                w1, idx1 = dp[i + 1][k]
                w2_sub, idx2_sub = dp[j][k - 1]
                w2 = w + w2_sub
                idx2 = tuple(sorted((orig_idx,) + idx2_sub))
                if w1 > w2:
                    dp[i][k] = (w1, idx1)
                elif w2 > w1:
                    dp[i][k] = (w2, idx2)
                else:
                    if idx1 and idx2:
                        dp[i][k] = (w1, min(idx1, idx2))
                    elif idx1:
                        dp[i][k] = (w1, idx1)
                    else:
                        dp[i][k] = (w2, idx2)
        return list(dp[0][4][1])