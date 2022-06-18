class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        
        nums.sort()
        sum = 0
        for i in range(len(nums)):

            if (i % 2) == 0:
                continue
            
            sum += min(nums[i], nums[i-1])

        
        return sum