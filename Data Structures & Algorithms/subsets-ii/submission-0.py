class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(start, path):
            res.append(path.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                helper(i + 1, path + [nums[i]])
        helper(0, [])
        return res