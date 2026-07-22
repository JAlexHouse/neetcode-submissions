class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        col = -1

        while low < high:
            mid = low + (high - low) // 2
            if matrix[mid][0] < target:
                if mid + 1 < len(matrix) and matrix[mid + 1][0] > target:
                    low = mid
                    break
                else:
                    low = mid + 1
            elif matrix[mid][0] > target:
                if mid - 1 >= 0 and matrix[mid - 1][0] < target:
                    high = mid - 1
                    break
                else:
                    high = mid - 1
            else:
                return True
        
        col = low + (high - low) // 2
        print(col)
        row = matrix[col]

        low, high = 0, len(row) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if row[mid] > target:
                high = mid - 1
            elif row[mid] < target:
                low = mid + 1
            else:
                return True
        
        return False
            
        