class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        sol = []    # output 배열 변수 선언

        nums_cnt = Counter(nums)

        # value 값을 기준으로 내림차순으로 정렬
        nums_cnt = dict(sorted(nums_cnt.items(), key=lambda x:x[1], reverse=True))
    
        for key in nums_cnt:
            if k == 0:
                break
            sol.append(key)
            k -= 1

        return sol