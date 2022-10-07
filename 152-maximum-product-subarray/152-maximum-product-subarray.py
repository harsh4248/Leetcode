class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        curMax,curMin = 1,1
        res = max(nums)
        
        for val in nums:
            if val == 0:
                curMax,curMin = 1,1
                continue
            temp = curMax * val
            curMax = max(val,val*curMax,val*curMin)
            curMin = min(val,val*curMin,temp)
            res = max(res,curMax)
            
        
        return res
