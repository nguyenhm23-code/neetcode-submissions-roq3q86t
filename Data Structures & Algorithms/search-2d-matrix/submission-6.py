class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right :
            mid = (left + right)//2
            if matrix[mid][-1] == target or matrix[mid][0] == target:
                return True
            elif matrix[mid][-1] < target:
                left = mid + 1
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                break
        l, r = 0, len(matrix[mid]) - 1
        while l <= r:
            middle = (l + r)//2
            if matrix[mid][middle] == target:
                return True
            elif matrix[mid][middle] > target:
                r = middle - 1
            elif matrix[mid][middle] < target:
                l = middle + 1
        return False
                    

            
        