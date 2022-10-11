class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
        
        low = 0
        high = len(nums) - 1
        
        while(low <= high):
            
            mid = (low + high) // 2
            
            if(nums[mid] == target):
                return mid
            elif(nums[mid] >= nums[0]):
                if(target >= nums[0] and target < nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if(target <= nums[len(nums) - 1] and target > nums[mid]):
                    low = mid+1
                else:
                    high = mid - 1
                    
            print(mid)
                
        return -1
        
        
        