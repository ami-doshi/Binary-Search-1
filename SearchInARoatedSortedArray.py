#Binary Search, note:at each point, mid will have a sorted and a non-sorted array on either side. Check the target in the sorted array
#Time - O(Logn)
#Space - O(1)

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums is None:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0
        h = len(nums)-1
        
        while(l<=h):
            mid = l + (h-l)//2

            # Mid is found
            if target == nums[mid]:
                return mid

            #iterate on sorted side of the array, one side of mid will be sorted and one not

            #left is sorted
            if nums[l]<=nums[mid]:
                #if target lies between low and mid, 
                if nums[mid] >= target and nums[l] <= target:
                    h = mid - 1
                #if not move low to start of unsorted array
                else:
                    l = mid + 1

            #right is sorted    
            else:
                if nums[mid] <= target and nums[h] >= target:
                    l = mid +1
                else:
                    h = mid - 1

        return -1
        