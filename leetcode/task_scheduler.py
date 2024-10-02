# https://leetcode.com/problems/task-scheduler/description/
from typing import *
import heapq
from collections import Counter,deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        heap = []
        counter = Counter(tasks)
        for key,value in counter.items():
            heapq.heappush(heap,(-value,key))
        
        count = 0
        q = deque()
        while heap or q:
            # print(f'heap={heap}')
            if q and q[0][2]<= count:
                it = q.popleft()
                heapq.heappush(heap,(it[0],it[1]))
            if heap:
                value, label = heapq.heappop(heap)
                if value < -1:
                    q.append((value+1,label,count+n+1))
            # print(f'count={count} label={label} last_index={last_index}')
            count += 1
        return count
    
if __name__ == '__main__':
    s = Solution()
    print(s.leastInterval(["A","A","A","B","B","B"],2),8)
    print(s.leastInterval(["A","C","A","B","D","B"],1),6)
    print(s.leastInterval(["A","A","A", "B","B","B"],3),10)
    print(s.leastInterval(["A","B","A"],2),4)
    # A B _ A
    print(s.leastInterval(["A","A","A","B","B","B"],50),104)
    print(s.leastInterval(["A","A","A","A","A","A","B","C","D","E","F","G"],1),12)
    
            
            


