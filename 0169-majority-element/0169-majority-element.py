class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        half = len(nums) / 2
        

        num_count = Counter(nums)

        for num, value in num_count.items():
            if value >= half:
                sol = num


        
        return sol