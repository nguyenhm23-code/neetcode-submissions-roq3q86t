class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        while (l <= r):
            mid = (l + r)//2
            if matrix[mid][-1] < target :
                l = mid + 1 
            elif matrix[mid][0] > target :
                r = mid - 1
            else:
                break
        left = 0
        right = len(matrix[mid]) - 1
        while left <= right:
            middle = (left + right)//2
            if matrix[mid][middle] == target:
                return True
            elif matrix[mid][middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False 
            
        
            


            

