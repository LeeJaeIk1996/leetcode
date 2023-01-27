class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() # 매개변수를 정렬

        for index in range(len(nums) - 2):  # index를 기준으로 나머지 두 수는 뒤에서 찾을 것이기 때문에 len(nums) - 2의 범위까지 순회한다.
            # 중복된 값 건너뛰기
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            # 간격을 좁혀가며 합(sum) 계산
            left, right = index + 1, len(nums) - 1
            while left < right: # 왼쪽부터(index의 바로 다음부터 시작) 서서히 right(nums의 끝까지)까지 다가가며 right에 다다를 때 까지
                sum = nums[index] + nums[left] + nums[right]    # x + y + Z = 0이 될 경우 result에 추가
                if sum < 0:     # nums를 정렬하였으므로 left를 이동해야 sum의 값이 커지게 된다.
                    left += 1
                elif sum > 0:   # nums를 정렬하였으므로 right를 이동해야 sum의 값이 작아지게 된다.
                    right -= 1
                else:   # sum이 0이라는 뜻이기도 하다.
                    result.append([nums[index], nums[left], nums[right]])   # result에 추가
                
                    # left와 right 양 옆에 동일한 값이 있을 수 있으므로 left +=1, right -= 1을 반복해서 스킵하도록 처리
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # left가 right와 같아질 때 까지 포인터를 이동하면서 값을 찾는다.
                    left += 1
                    right -= 1


        return result   # 결과 반환