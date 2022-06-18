class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        resultlist : list = []  # 출력할 리스트 생성
        nums.sort()

        for i in range(len(nums) -2):
            # 중복 값 제거
            if i > 0 and nums[i] == nums[i-1]:
                continue


            # 투 포인터를 활용
            left, right = i + 1, len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    resultlist.append([nums[i], nums[left], nums[right]])

                    # left와 right 양 옆에 같은 값이 있을 수 있으므로 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left +=1
                    while left < right and nums[right] == nums[right - 1]:
                        right -=1
                        
                    left +=1
                    right -= 1

        return resultlist