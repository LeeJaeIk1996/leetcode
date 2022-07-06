class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        storage = collections.Counter(nums)
        storage_heap = []

        # 힙에 음수로 삽입
        for i in storage:
            # (우선순위, 값) -> heapq는 min heap이기 때문에 max heap으로 바꾸기 위해 음수로 우선순위를 지정
            heapq.heappush(storage_heap, (-storage[i], i))

        
        result = []
        # k번 만큼 추출, min heap이므로 가장 작은 음수 순으로 추출
        for _ in range(k):
            result.append(heapq.heappop(storage_heap)[1])

        
        return result

        