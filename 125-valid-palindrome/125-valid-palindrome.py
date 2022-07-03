class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palin = collections.deque()
     
        # input의 s를 소문자들로 정리하여 리스트에 삽입
        for char in s:
            if char.isalnum():
                palin.append(char.lower())

        # 팰린드롬 판별
        while len(palin) > 1:
            if palin.popleft() != palin.pop():
                return False

        return True