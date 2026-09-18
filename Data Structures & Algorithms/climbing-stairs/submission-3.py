from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def ways(remaining: int) -> int:
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            return ways(remaining - 1) + ways(remaining - 2)

        return ways(n)