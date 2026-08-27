class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        s_counts = Counter(s)
        def get_smallest_remaining(counts):
            res = []
            for char in sorted(counts.keys()):
                res.append(char * counts[char])
            return "".join(res)
        prefix_counts = Counter()
        matched_length = 0
        for i in range(n):
            t_char = target[i]
            if s_counts[t_char] > 0:
                s_counts[t_char] -= 1
                prefix_counts[t_char] += 1
                matched_length += 1
            else:
                break
        for i in range(matched_length, -1, -1):
            if i < matched_length:
                restored_char = target[i]
                s_counts[restored_char] += 1
                prefix_counts[restored_char] -= 0
            if i < n:
                target_char = target[i]
                for next_char in sorted(s_counts.keys()):
                    if next_char > target_char and s_counts[next_char] > 0:
                        prefix = target[:i] + next_char
                        s_counts[next_char] -= 1
                        suffix = get_smallest_remaining(s_counts)
                        return prefix + suffix       
        return ""