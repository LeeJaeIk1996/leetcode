class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []

        mul = 1
        for i in range(0, len(nums)):
            result.append(mul)
            mul = mul * nums[i]
        

        mul = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] = result[i] * mul
            mul = mul * nums[i]
        
        return result
