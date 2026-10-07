class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def isValid(string: str) -> bool:
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0
        if isValid(s):
            return [s]
        queue = deque([s])
        visited = {s}
        found = False
        result = []
        while queue and not found:
            level_size = len(queue)
            current_level_valid = []
            for _ in range(level_size):
                current = queue.popleft()
                for i in range(len(current)):
                    if current[i] not in ('(', ')'):
                        continue
                    next_state = current[:i] + current[i+1:]
                    if next_state not in visited:
                        visited.add(next_state)
                        if isValid(next_state):
                            current_level_valid.append(next_state)
                        else:
                            queue.append(next_state)
            if current_level_valid:
                result = list(set(current_level_valid))
                found = True
        return result if result else [""]