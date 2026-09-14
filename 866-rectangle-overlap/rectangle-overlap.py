class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        is_left = rec1[2] <= rec2[0]
        is_right = rec1[0] >= rec2[2]
        is_below = rec1[3] <= rec2[1]
        is_above = rec1[1] >= rec2[3]
        return not (is_left or is_right or is_below or is_above)