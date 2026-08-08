class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # since matrix is sorted, we just use binary search to reduce time complexity
        # get dimensions and treat matrix like one giant array
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS * COLS - 1 # using dimension of columns
        while l <= r:
            # left, right and middle ptr
            m = l + (r - l) // 2 
            row, col = m // COLS, m % COLS
            
            if target > matrix[row][col]:
                l = m + 1
            elif target < matrix[row][col]:
                r = m - 1
            else:
                return True
        return False
