class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litters = []
        start_r = start_c = -1
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start_r, start_c = r, c
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
        total_litter = len(litters)
        litter_map = {pos: i for i, pos in enumerate(litters)}
        target_mask = (1 << total_litter) - 1
        initial_mask = 0
        if (start_r, start_c) in litter_map:
            initial_mask |= (1 << litter_map[(start_r, start_c)])
        if initial_mask == target_mask:
            return 0
        queue = deque([(start_r, start_c, energy, initial_mask, 0)])
        visited = {(start_r, start_c, initial_mask): energy}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            r, c, curr_energy, mask, moves = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and classroom[nr][nc] != 'X':
                    next_energy = curr_energy - 1
                    if next_energy < 0:
                        continue
                    is_reset = (classroom[nr][nc] == 'R')
                    n_energy = energy if is_reset else next_energy
                    n_mask = mask
                    if classroom[nr][nc] == 'L':
                        n_mask |= (1 << litter_map[(nr, nc)])
                    if n_mask == target_mask:
                        return moves + 1
                    if n_energy == 0 and not is_reset:
                        continue
                    state_key = (nr, nc, n_mask)
                    if state_key not in visited or visited[state_key] < n_energy:
                        visited[state_key] = n_energy
                        queue.append((nr, nc, n_energy, n_mask, moves + 1))
        return -1