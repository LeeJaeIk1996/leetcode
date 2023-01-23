class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        cnt = 1
        start = 0
        sequence = []
    

        sorted_nums = sorted(nums)
        
        if sorted_nums is None:
            return 0

        for i in range(len(sorted_nums)):
            if i+1 < len(sorted_nums) and sorted_nums[i] + 1 == sorted_nums[i+1]:
                cnt += 1
            elif i+1 < len(sorted_nums) and sorted_nums[i] == sorted_nums[i+1]:
                cnt += 0
            else:
                sequence.append(cnt)
                cnt = 1

        return max(sequence, default = 0)
                