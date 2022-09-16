class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for i in nums:
            total += i
            
        currsum = 0
        for i in range(0,len(nums)):
            if(currsum == total - nums[i]):
                return i
            currsum += nums[i]
            total -= nums[i]
            
        return -1
        