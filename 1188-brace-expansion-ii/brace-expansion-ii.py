class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        groups = [[]]
        level = 0
        start = 0
        for i, c in enumerate(expression):
            if c == '{':
                if level == 0:
                    start = i + 1
                level += 1
            elif c == '}':
                level -= 1
                if level == 0:
                    inner = self.braceExpansionII(expression[start:i])
                    if not groups[-1]:
                        groups[-1] = inner
                    else:
                        groups[-1] = [x + y for x in groups[-1] for y in inner]
            elif level == 0:
                if c == ',':
                    groups.append([])
                else:
                    if not groups[-1]:
                        groups[-1] = [c]
                    else:
                        groups[-1] = [x + c for x in groups[-1]]
        res = set()
        for g in groups:
            for word in g:
                res.add(word)
        return sorted(list(res))