# Binary Search - Assuming 2D array as 1D
# Time Complexity: O(logmn)
# Space Complexity = O(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == None or len(matrix) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        #if single element matrix
        if m == 1 and n == 1: 
            if matrix[0][0] == target:
                return True
            else:
                return False
        
        #imagine the matrix is a single 1D array and you are doing Binary Search on it
        h = m*n - 1
        l = 0
        
        while(h>=l):
            mid = l + (h-l)//2 #element 5 is the middle of element 1 and 10 (position 0 and 4)
           # print(l,mid,h)
            
            #we divide and modulo from N i.e. number of elements in a row to find row and column position
            r = mid // n # element 5 is on position 2 in single array... 2//4 == 0 i.e. its on 0th row
            c = mid % n # element 5 is on position 2 in single array... 2%4 == 2 i.e. its on 3rd column
            #print(r,c,matrix[r][c])
            #print()
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                l = mid + 1
            else:
                h = mid - 1
                
        # if we dont find element
        return False
            
            