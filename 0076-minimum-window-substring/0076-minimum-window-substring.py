class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 필요한 문자 각각의 개수
        need = Counter(t)
        # 필요한 문자 전체 개수
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동 (오른쪽 포인터이므로 1부터 시작한다.)
        for right, char in enumerate(s, 1):
            # 현재 문자가 필요한 문자 need[char]에 포함되어 있다면 missing과 need[char]를 1 감소시킨다.
            missing -= need[char] > 0
            need[char] -= 1

            # 필요한 문자가 0이면 왼쪽 포인터를 이동
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1

                if not end or right - left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start:end]
        