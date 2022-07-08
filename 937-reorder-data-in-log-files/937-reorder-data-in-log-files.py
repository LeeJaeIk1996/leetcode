class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        number : list = []
        letter : list = []

        # 식별자 뒤 문자와 숫자 여부를 확인한 후 각각 다른 리스트에 추가
        for log in logs:
            if log.split()[1].isdigit():
                number.append(log)
            else:
                letter.append(log)

        
        # 2개의 key를 람다 표현식으로 정렬
        letter.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letter + number
