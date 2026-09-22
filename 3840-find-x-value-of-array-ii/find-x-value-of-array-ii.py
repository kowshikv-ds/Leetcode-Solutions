class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [None] * (4 * n)
        arr = [x % k for x in nums]
        def merge(left, right):
            if not left: return right
            if not right: return left
            l_prod, l_remains = left
            r_prod, r_remains = right
            merged_prod = (l_prod * r_prod) % k
            merged_remains = l_remains.copy()
            for r_rem, count in r_remains.items():
                actual_rem = (l_prod * r_rem) % k
                merged_remains[actual_rem] = merged_remains.get(actual_rem, 0) + count
            return (merged_prod, merged_remains)
        def build(node, start, end):
            if start == end:
                val = arr[start]
                tree[node] = (val, {val: 1})
                return
            mid = (start + end) // 2
            build(2 * node + 1, start, mid)
            build(2 * node + 2, mid + 1, end)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])
        def update(node, start, end, idx, val):
            if start == end:
                val_mod = val % k
                arr[idx] = val_mod
                tree[node] = (val_mod, {val_mod: 1})
                return
            mid = (start + end) // 2
            if start <= idx <= mid:
                update(2 * node + 1, start, mid, idx, val)
            else:
                update(2 * node + 2, mid + 1, end, idx, val)
            tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])
        def query(node, start, end, l, r):
            if r < start or end < l:
                return None
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            left_res = query(2 * node + 1, start, mid, l, r)
            right_res = query(2 * node + 2, mid + 1, end, l, r)
            return merge(left_res, right_res)
        build(0, 0, n - 1)
        result = []
        for index, value, start, x in queries:
            update(0, 0, n - 1, index, value)
            _, remains = query(0, 0, n - 1, start, n - 1)
            result.append(remains.get(x, 0))
        return result