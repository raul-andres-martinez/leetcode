from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        coins = 0
        n = len(piles) // 3
        for i in range(n):
            coins += piles[-(2 * (i + 1))]
        return coins

print(Solution().maxCoins([2,4,5]))