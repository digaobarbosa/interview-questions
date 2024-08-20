# https://leetcode.com/problems/min-stack/description/
from typing import *
import heapq

class MinStack:



    def __init__(self):
        self.stack = []
        self.q = []


    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.q,val)


    def pop(self) -> None:
        v = self.stack.pop()
        self.q.remove(v)
        heapq.heapify(self.q)



    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.q[0]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())