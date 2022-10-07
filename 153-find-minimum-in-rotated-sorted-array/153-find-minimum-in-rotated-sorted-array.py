class Solution:
    def findMin(self, nums: List[int]) -> int:
        
#         i = 0
        if(len(nums) == 1):
            return nums[0]
        
#         while True:
#             if(nums[i] > nums[(i+1) % len(nums)]):
#                 return nums[(i+1) % len(nums)]
            
#             i = (i+1)%len(nums)
        
    
        low = 0
        high = len(nums) - 1
        if nums[high] > nums[0]:
            return nums[0]
        while(low <= high):
            
            mid = low + (high - low) // 2
            
            if(nums[mid] > nums[mid + 1]):
                return nums[mid + 1]
            if(nums[mid - 1] > nums[mid]):
                return nums[mid]
            
            elif(nums[mid] > nums[0]):
                low = mid + 1
            else:
                high = mid - 1
        