class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 인덱스를 찾는 문제이므로 enumerate 활용
        for i, n in enumerate(nums):
            
            two = target - n
            
            if two in nums[i + 1:]:
                return [i, nums.index(two, nums.index(n)+1)]