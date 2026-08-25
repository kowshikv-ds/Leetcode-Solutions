class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        temp = k
        while True:
            if temp not in nums:
                return temp
            temp += k