class MyCircularDeque:

    def __init__(self, k: int):
        """MyCircularDeque 생성자"""
        # head는 제일 앞의 ListNode를, tail은 제일 뒤의 ListNode를 가리키고 있다.
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        # 초기에 아무것도 없으므로 head와 tail을 서로 연결시켜준다.
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        """이중 연결 리스트에 신규 노드 삽입"""
        tmp = node.right
        node.right.left = new
        node.right = new
        new.left = node
        new.right = tmp

    def _del(self, node: ListNode):
        """이중 연결 리스트에 노드 삭제"""
        n = node.right.right
        node.right = n
        n.left = node
        
    def insertFront(self, value: int) -> bool:
        """데크 처음에 아이템을 추가하는 함수"""
        if self.len == self.k:
            return False
        self._add(self.head, ListNode(value))
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        """데크 마지막에 아이템을 추가하는 함수"""
        if self.len == self.k:
            return False
        self._add(self.tail.left, ListNode(value))
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        """데크 처음 아이템을 삭제하는 함수"""
        if self.len == 0:
            return False
        self._del(self.head)
        self.len -=1
        return True

    def deleteLast(self) -> bool:
        """데크 마지막 아이템을 삭제하는 함수"""
        if self.len == 0:
            return False
        self._del(self.tail.left.left)
        self.len -=1
        return True

    def getFront(self) -> int:
        """데크의 첫 번째 아이템을 가져오는 함수"""
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        """데크의 마지막 아이템을 가져오는 함수"""
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        """데크가 비어 있는지 여부를 판별"""
        return self.len == 0
        

    def isFull(self) -> bool:
        """데크가 가득 차 있는지 여부를 판별"""
        return self.len == self.k