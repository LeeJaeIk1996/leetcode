class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
         
        answer = []
        mul = 1

        # 왼쪽부터
        for i in range(0, len(nums)):
            answer.append(mul)
            mul = mul * nums[i]

        mul = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] = answer[i] * mul
            mul = mul * nums[i]

        return answer