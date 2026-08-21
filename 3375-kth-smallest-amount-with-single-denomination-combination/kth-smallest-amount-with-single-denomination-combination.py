class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        for mask in range(1, 1 << n):
            current_lcm = 1
            bits_count = 0
            for i in range(n):
                if (mask >> i) & 1:
                    bits_count += 1
                    current_lcm = (current_lcm * coins[i]) // math.gcd(current_lcm, coins[i])
            sign = 1 if bits_count % 2 == 1 else -1
            subsets.append((current_lcm, sign))

        def count_valid(m: int) -> int:
            total = 0
            for lcm, sign in subsets:
                total += sign * (m // lcm)
            return total

        low = 1
        high = min(coins) * k
        answer = high
        while low <= high:
            mid = low + (high - low) // 2
            if count_valid(mid) >= k:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer