class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # stones을 넣을 해시 테이블
        case = {}

        # 출력값 계산
        count = 0

        # stones의 문자 갯수를 계산
        for s in stones:
            if s not in case:
                case[s] = 1
            else:
                case[s] += 1

        # case에 들어 있는 stones에서 jewels를 계산
        for j in jewels:
            if j in case:
                count += case[j]

        return count
