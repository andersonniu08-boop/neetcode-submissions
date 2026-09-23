class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def backtrack(start: int, remain: int, path: list[int]):
            if remain == 0:
                res.append(path.copy())
                return
            for i in range(start, len(nums)):
                if nums[i] > remain:
                    break
                path.append(nums[i])
                backtrack(i, remain - nums[i], path)
                path.pop()
        backtrack(0, target, [])
        return res