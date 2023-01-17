class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # dfs 재귀 함수 생성
        def dfs(index, path):
            # 끝까지 탐색할 경우 백트래킹
            if len(path) == len(digits):
                result.append(path)
                # 함수 호출을 종료
                return 

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i + 1, path + j)
    
        if not digits:
            return []
        
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        dfs(0, "")

        return result