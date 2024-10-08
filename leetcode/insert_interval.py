# https://leetcode.com/problems/insert-interval/
from typing import *

class Solution_inplace:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted_pos = None
        i = 0
        while i < len(intervals):
            x = intervals[i]
            if inserted_pos is not None:
                if newInterval[1] < x[0]:
                    break
                elif newInterval[1] <= x[1] or newInterval[1] ==  x[0]:
                    intervals[inserted_pos][1] = x[1]
                    intervals.pop(i)
                    break
                else:
                    intervals.pop(i)
                    continue
            elif x[0] >= newInterval[0] or x[1] >= newInterval[0]:
                if newInterval[1] < x[0] :
                    intervals.insert(i,newInterval)
                    inserted_pos = i
                    break
                if newInterval[1] ==  x[0]:
                    x[0] = newInterval[0]
                    inserted_pos = i
                elif newInterval[1] <= x[1]:
                    x[0] = min(newInterval[0],x[0])
                    inserted_pos = i
                    break
                elif newInterval[1] > x[1]:
                    inserted_pos = i
                    x[0] = min(newInterval[0],x[0])
                    x[1] = max(newInterval[1],x[1])
                elif newInterval[0] == x[1]:
                    inserted_pos = i
                    x[0] = min(newInterval[0],x[0])
                    x[1] = max(newInterval[1],x[1])
                    break
            i += 1
        if inserted_pos is None:
            intervals.append(newInterval)
        return intervals
            
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted_pos = None
        for i in range(len(intervals)):
            it = intervals[i]
            if inserted_pos is None:
                if newInterval[1] < it[0] :
                    res.append(newInterval)
                    res.append(it)
                    inserted_pos = i
                elif newInterval[1] >= it[0] and newInterval[1]<=it[1]:
                    res.append([min(newInterval[0],it[0]),it[1]])
                    inserted_pos = i
                elif newInterval[1] > it[1] and newInterval[0] <= it[1]:
                    newInterval = [min(newInterval[0],it[0]),newInterval[1]]
                else:
                    res.append(it)
            else:
                res.append(it)
        if inserted_pos is None:
            res.append(newInterval)
        return res
                

        


s = Solution()
print(s.insert([[1,3],[6,9]],[2,5]))            
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))
print(s.insert([],[4,8]))
print(s.insert([[1,9]],[4,8]))
print(s.insert([[1,5]],[5,8]))
print(s.insert([[1,5]],[0,1]))
print(s.insert([[1,5]],[0,0]))
                    
                
        
        