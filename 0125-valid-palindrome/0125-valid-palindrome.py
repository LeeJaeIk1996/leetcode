class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = []

        for char in s:
            if char.isalnum():  # 문자열의 해당 위치가 문자인 경우
                str.append(char.lower())    # 소문자로 변환하여 문자를 저장

        last = len(str) - 1
        for first in range(len(str)):
            print(first, last)
            if (last > first) and (str[first] == str[last]):
                last -= 1
                continue
            elif (last == first) or (first > last): # 종료 조건
                break
            else:
                return False
            
        
        return True



