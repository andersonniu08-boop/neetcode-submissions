class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        left_row, left_column = 0, 0
        right_row, right_column = len(matrix) - 1, len(matrix[0]) - 1
        if matrix[right_row][right_column] == target or matrix[left_row][left_column] == target:
            return True
        while not left_row == right_row:
            if matrix[left_row][right_column] < target:
                left_row += 1
            elif matrix[right_row][left_column] > target:
                right_row -= 1


        while right_column > left_column:
            if matrix[left_row][left_column] < target:
                left_column += 1
            elif matrix[left_row][right_column] > target:
                right_column -= 1

        return matrix[left_row][left_column] == target