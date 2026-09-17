class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l + 1 < h:
            mid = l + (h - l) // 2

            if nums[mid] == target:
                return mid

            # 1. Check if left half [l ... mid] is sorted
            if nums[l] < nums[mid]:
                # If target is inside the left half's bounds
                if nums[l] <= target < nums[mid]:
                    h = mid 
                else:
                    l = mid 
            # 2. Otherwise, right half [mid ... h] must be sorted
            else:
                # If target is inside the right half's bounds
                if nums[mid] < target <= nums[h]:
                    l = mid 
                else:
                    h = mid 

        if nums[l] == target:
            return l
        if nums[h] == target:
            return h
            
        return -1
        