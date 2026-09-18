class Solution:
  def maxNumOfSubstrings(self, s: str) -> list[str]:
    n = len(s)
    left = [n] * 26
    right = [-1] * 26
    for i, ch in enumerate(s):
      idx = ord(ch) - ord('a')
      left[idx] = min(left[idx], i)
      right[idx] = max(right[idx], i)
    def get_valid_range(i):
      l, r = left[i], right[i]
      j = l
      while j <= r:
        char_idx = ord(s[j]) - ord('a')
        if left[char_idx] < l:
          return -1
        r = max(r, right[char_idx])
        j += 1
      return r
    intervals = []
    for i in range(26):
      if left[i] != n:
        r = get_valid_range(i)
        if r != -1:
          intervals.append((left[i], r))
    intervals.sort(key=lambda x: x[1])
    result = []
    prev_end = -1
    for l, r in intervals:
      if l > prev_end:
        result.append(s[l : r + 1])
        prev_end = r
    return result