class MedianFinder:

    def __init__(self):
        self.sol = []
        
    def addNum(self, num: int) -> None:
        self.sol.append(num)
        # 숫자를 추가하였으므로 median을 구하기 위해 정렬해준다.
        
    def findMedian(self) -> float:
        self.sol.sort()
        # 만약 배열 sol의 길이가 짝수일 경우 두 중간 값의 평균을 반환
        if (len(self.sol) % 2) == 0:
            return (self.sol[(len(self.sol) // 2) - 1] + self.sol[len(self.sol) // 2]) / 2

        # 만약 배열 sol의 길이가 홀수일 경우 중간 값을 반환
        else:
            return self.sol[len(self.sol) // 2]