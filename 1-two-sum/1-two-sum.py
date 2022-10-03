class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         The most basic solution will be an brute approach
#         using two for loops
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i,j]
        
        