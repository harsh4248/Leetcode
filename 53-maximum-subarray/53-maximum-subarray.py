class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum,maxSum = nums[0],nums[0]
        
        for i in range(1,len(nums)):
            curSum += nums[i]
            if(curSum < nums[i]):
                curSum = nums[i]
            if(maxSum < curSum):
                maxSum = curSum
            
        
        
        return maxSum