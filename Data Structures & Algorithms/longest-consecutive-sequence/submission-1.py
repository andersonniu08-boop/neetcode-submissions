class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(sorted(nums))
        longest_streak = 0
        for num in hashset:
            if num - 1 not in hashset:
                curr_num = num
                curr_streak = 1
                while curr_num + 1 in hashset:
                    curr_num += 1
                    curr_streak += 1
                longest_streak = max(curr_streak, longest_streak)
        return longest_streak


        