class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path, remaining):
            if not remaining:
                res.append(path)
                return
            for x in remaining:
                helper(path + [x], remaining - {x})
        
        helper([], set(nums))
        return res