class MyStack(object):

    def __init__(self):
        self.stack = collections.deque()

    def push(self, x):  # 요소 x를 스택에 삽입한다.
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        for _ in range(len(self.stack) - 1):
            self.stack.append(self.stack.popleft())
        

    def pop(self):  # 스택의 첫 번째 요소를 삭제한다
        """
        :rtype: int
        """
        return self.stack.popleft()
        

    def top(self):  # 스택의 첫 번째 요소를 가져온다        
        """
        :rtype: int
        """
        return self.stack[0]
        

    def empty(self):    # 스택이 비어 있는지 확인한다
        """
        :rtype: bool
        """
        return len(self.stack) == 0
        
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()