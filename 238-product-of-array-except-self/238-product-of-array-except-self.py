class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = 1
        countZero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countZero += 1
                continue
            ans *= nums[i]
        
        if countZero > 1:
            return [0] * len(nums)
        
        else:
            for i in range(len(nums)):
                if(nums[i] == 0):
                    temp = [0] * len(nums)
                    temp[i] = ans
                    return temp
                nums[i] = ans // nums[i]
            
            return nums
        
        
            
        
        
        