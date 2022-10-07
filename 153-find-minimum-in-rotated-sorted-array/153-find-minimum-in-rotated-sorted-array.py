class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        i = 0
        if(len(nums) == 1):
            return nums[0]
        
        while True:
            if(nums[i] > nums[(i+1) % len(nums)]):
                return nums[(i+1) % len(nums)]
            
            i = (i+1)%len(nums)
        
        