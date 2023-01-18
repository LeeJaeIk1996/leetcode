class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        used = {}
        # 투 포인터를 사용
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 최대 부분 문자열 길이 갱신
            else:
                max_length = max(max_length, index - start + 1)

            # 현재 문자의 위치 삽입
            used[char] = index

        return max_length