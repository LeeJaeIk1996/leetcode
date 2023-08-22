class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits: List = []
        letters: List = []

        # 문자로 구성된 로그와 숫자로 구성된 로그를 나눠 배열에 저장
        for log in logs:
            if log.split()[1].isdigit():    # 숫자인 경우
                digits.append(log)
            else:   # 문자인 경우
                letters.append(log) 

        # 문자로 구성된 로그들을 규칙에 맞게 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letters + digits