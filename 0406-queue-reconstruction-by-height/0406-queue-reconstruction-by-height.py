class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap: list = []

        # 최대 힙 push
        for peoples in people:
            heappush(heap, (-peoples[0], peoples[1]))   # (우선순위, 값)으로 구성된 튜플

        result: list = []

        # 최대 힙 pop
        while heap:
            peoples = heappop(heap)
            result.insert(peoples[1], [-peoples[0], peoples[1]])

        
        return result