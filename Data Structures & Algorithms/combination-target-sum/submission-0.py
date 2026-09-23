class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i, carry):
            if carry == target:
                res.append(subset.copy())
                return
            if carry > target or i >= len(nums):
                return

            #include in subset
            subset.append(nums[i])
            dfs(i, carry + nums[i])
            #dont include
            subset.pop()
            dfs(i + 1, carry)
        
        dfs(0, 0)

        return res