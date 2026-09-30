class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def helper(idx):
            if idx >= n:
                return 0
            if idx in memo:
                return memo[idx]
            memo[idx] = cost[idx] + min(helper(idx + 1), helper(idx + 2))
            return memo[idx]
        return min(helper(0), helper(1))
