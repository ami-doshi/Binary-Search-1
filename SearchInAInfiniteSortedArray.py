# two step process: 1. finding boundary (Trick is the bit shift for faster execution), 2. binary search in boundary found
# Time Complexity: O(logn) - each is logn --> simple binary and boundary finding
# Space Complexity: O(1) 


# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        
        #initial boundary
        l = 0
        h = 1
        
        #if in initial array
        if target < reader.get(h):        
            if target == reader.get(l):
                return l
            if target == reader.get(h):
                return h
        
        while (target > reader.get(h)):
            #x << y: Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2**y.
            l = h+1
            h = h << 2    
            
        #Binary Search
        
        while (l<=h):
            mid = l + (h-l)//2
            val = reader.get(mid)
            if  val == target:
                return mid
            if target <= val:
                h = mid - 1
            else:
                l = mid + 1
                
        return -1
        
        
            

        
            
            
        