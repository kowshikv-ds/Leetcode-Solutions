class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rs = {}
        grps = 0
        for row, seat in reservedSeats:
            if row not in rs: rs[row] = []
            rs[row].append(seat)
        for i in rs:
            rs[i].sort()
            if 10 not in rs[i]: rs[i].append(10)
            if rs[i][0] != 1: rs[i].insert(0, 1)
            left = all(seat not in rs[i] for seat in (2, 3, 4, 5))
            right = all(seat not in rs[i] for seat in (6, 7, 8, 9))
            middle = all(seat not in rs[i] for seat in (4, 5, 6, 7))
            if left and right: grps += 2
            elif left or right or middle: grps += 1
        emptyRows = n - len(rs)
        grps += emptyRows * 2
        return grps