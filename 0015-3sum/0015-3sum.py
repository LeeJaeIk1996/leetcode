class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        # nums 배열을 순회. 
        for i in range(len(nums) - 2):
            # 중복된 값 제거
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i + 1
            right = len(nums) - 1

            # i를 기준으로 조건이 충족될 때까지 순회
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:   # sum = 0인 경우
                    answer.append([nums[i], nums[left], nums[right]])

                    # 동일한 값을 제거하기 위해 반복
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1

        return answer

                



