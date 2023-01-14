class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            sol = target - i    
            if sol in nums[nums.index(i)+1:]:
                return [nums.index(i), nums.index(sol, nums.index(i)+1)]