class Solution:
    _LOOKUP = [0] * 123
    for i in range(26):
        _LOOKUP[97 + i] = 26 - i
    def reverseDegree(self, s: str) -> int:
        lookup = self._LOOKUP
        return sum(lookup[code] * i for i, code in enumerate(s.encode('ascii'), 1))