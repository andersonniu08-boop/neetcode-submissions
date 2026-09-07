class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #indices * lowest heights of the indices
        i = 0
        j = len(heights) - 1
        max_area = 0
        while i < j:
            distance = j - i
            curr_area = distance * min(heights[i], heights[j])
            if curr_area > max_area:
                max_area = curr_area
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area
            



        