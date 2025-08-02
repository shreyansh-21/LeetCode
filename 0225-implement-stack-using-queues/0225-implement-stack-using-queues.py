from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if not self.q1:
            return -1 #(LeetCode expects -1 for edge cases)
        
        # Move all elements except last from q1 to q2
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        popped = self.q1.popleft()# The last element in q1 is our stack's top
        self.q1, self.q2 = self.q2, self.q1 # Swap q1 and q2 so q1 always holds the elements
        return popped

    def top(self) -> int:
        if not self.q1:
            return -1
        
        # Similar to pop() but we need to keep the element
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        
        top_element = self.q1[0]
        self.q2.append(self.q1.popleft())
        # Swap queues
        self.q1, self.q2 = self.q2, self.q1
        
        return top_element

    def empty(self) -> bool:
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()