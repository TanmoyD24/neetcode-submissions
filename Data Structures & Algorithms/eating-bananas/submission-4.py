class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        n = len(piles)

        def caneat(piles: List[int], mid: int) -> int:
            count = 0
            for i in range(n):
                if(piles[i] % mid == 0):
                    count += piles[i] // mid
                else:
                    count += (piles[i] // mid) + 1
            return count

        if (n == h):
            return high
            
        while(low <= high):
            mid = low + (high - low) // 2
            x = caneat(piles, mid)
            if(x > h):
                low = mid + 1
            else:
                high = mid - 1
        return low