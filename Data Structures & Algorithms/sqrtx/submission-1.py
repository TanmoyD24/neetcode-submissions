class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0 or x == 1):
            return x

        low = 1
        high = (x // 2) + 1

        while(low <= high):
            mid = low + (high - low) // 2
            n = mid * mid
            if(n == x):
                return mid
            if(n > x):
                high = mid -1
            else:
                low = mid + 1
        return high