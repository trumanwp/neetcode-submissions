class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        - 2d array, increasing numbers (binary search)
        - define l and r as first and last array in the 2d array
        - define mid as the middle array
        - check if target is in the mid array
        - if not, move array
        """

        left,right = 0, len(matrix)-1

        while left <= right:
            mid = (left + right) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                ml, mr = 0, len(matrix[mid]) - 1

                while ml <= mr:
                    mm = (ml + mr) // 2
                    if target > matrix[mid][mm]:
                        ml = mm + 1
                    elif target < matrix[mid][mm]:
                        mr = mm - 1
                    else:
                        return True
                
                return False
            
            elif target > matrix[mid][-1]:
                left = mid + 1
            elif target < matrix[mid][0]:
                right = mid - 1
        
        return False