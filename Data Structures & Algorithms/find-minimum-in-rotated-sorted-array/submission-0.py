class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if num is higher in the middle min has to be to the right
        l = 0
        h = len(nums) - 1
        while h > l:
            mid = (h + l) // 2
            if nums[mid] > nums[h]:
                l = mid + 1
            else:
                h = mid
            
        return nums[l]