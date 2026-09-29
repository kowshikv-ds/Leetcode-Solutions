class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        if (m + n) % 2 == 0 or grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False
        memo = {}
        def dfs(r, c, balance):
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1
            if balance < 0:
                return False
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if balance > remaining_steps:
                return False
            if r == m - 1 and c == n - 1:
                return balance == 0
            state = (r, c, balance)
            if state in memo:
                return memo[state]
            res = False
            if r + 1 < m:
                res = res or dfs(r + 1, c, balance)
            if c + 1 < n:
                res = res or dfs(r, c + 1, balance)
            memo[state] = res
            return res
        return dfs(0, 0, 0)