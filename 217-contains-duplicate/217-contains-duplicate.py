class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i] == nums[j]):
#                     return True
        
#         return False
        numCount = {}
        for val in nums:
            if val in numCount:
                return True
            else:
                numCount[val] = True
        
        return False
        