class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        indexed_nums = sorted((val, i) for i, val in enumerate(nums))
        groups = []
        current_group = []
        for val, idx in indexed_nums:
            if not current_group or val - current_group[-1][0] <= limit:
                current_group.append((val, idx))
            else:
                groups.append(current_group)
                current_group = [(val, idx)]
        if current_group:
            groups.append(current_group)
        res = [0] * n
        for group in groups:
            values = sorted([val for val, idx in group])
            indices = sorted([idx for val, idx in group])
            for i in range(len(group)):
                res[indices[i]] = values[i]
        return res