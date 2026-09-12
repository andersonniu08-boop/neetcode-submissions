#ai solution

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        h = len(nums) - 1

        while l <= h:
            mid = (l + h) // 2

            if nums[mid] == target:
                return mid

            # 1. Check if left half [l ... mid] is sorted
            if nums[l] <= nums[mid]:
                # If target is inside the left half's bounds
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                else:
                    l = mid + 1
            # 2. Otherwise, right half [mid ... h] must be sorted
            else:
                # If target is inside the right half's bounds
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1

        return -1