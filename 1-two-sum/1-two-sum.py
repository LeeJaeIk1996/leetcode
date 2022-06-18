class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        nums_map = {}
        
        for i, n in enumerate(nums):
            if target - n in nums_map:
                return [nums_map[target - n], i]
            nums_map[n] = i
        