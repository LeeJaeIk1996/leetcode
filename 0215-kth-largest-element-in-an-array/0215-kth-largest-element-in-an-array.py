class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # 매개변수 num 배열을 내림차순으로 정렬
        nums.sort(reverse=True)   

        for index in range(len(nums)):

            if index == k - 1:
                sol = nums[index]

        return sol