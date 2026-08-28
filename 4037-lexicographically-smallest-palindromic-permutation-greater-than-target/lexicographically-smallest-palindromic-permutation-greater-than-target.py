class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        count = Counter(s)
        odd_chars = [k for k, v in count.items() if v % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        mid_char = odd_chars[0] if odd_chars else ""
        if mid_char:
            count[mid_char] -= 1
        avail_pool = []
        for ch, freq in count.items():
            avail_pool.extend([ch] * (freq // 2))
        avail_counts = Counter(avail_pool)
        half_len = n // 2
        
        def try_build(prefix_len, divergence_char):
            rem_avail = Counter(avail_counts)
            res_half = []
            for i in range(prefix_len):
                ch = target[i]
                if rem_avail[ch] > 0:
                    rem_avail[ch] -= 1
                    res_half.append(ch)
                else:
                    return None
            if divergence_char:
                if rem_avail[divergence_char] > 0:
                    rem_avail[divergence_char] -= 1
                    res_half.append(divergence_char)
                else:
                    return None
            sorted_rem = sorted(rem_avail.elements())
            res_half.extend(sorted_rem)
            half_str = "".join(res_half)
            full_palindrome = half_str + mid_char + half_str[::-1]
            return full_palindrome if full_palindrome > target else None
        valid_candidates = []
        p_exact = try_build(half_len, None)
        if p_exact:
            valid_candidates.append(p_exact)
        for i in range(half_len):
            start_char_code = ord(target[i]) + 1
            for code in range(start_char_code, ord('z') + 1):
                ch = chr(code)
                p_diverge = try_build(i, ch)
                if p_diverge:
                    valid_candidates.append(p_diverge)
                    break
        return min(valid_candidates) if valid_candidates else ""