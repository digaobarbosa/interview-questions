# https://leetcode.com/problems/course-schedule/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:

    def depth_has_cycle(self, requisites, course, visited: set, visiting: set):
        if course in visited:
            return False
        if course in visiting:
            return True
        visiting.add(course)
        for req in requisites[course]:
            res = self.depth_has_cycle(requisites, req, visited, visiting)
            if res:
                return True
        visited.add(course)
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        requisites = [[] for i in range(numCourses)]
        for course, pre in prerequisites:
            requisites[course].append(pre)
        visited = set()
        visiting = set()
        for i in range(len(requisites)):

            for j in requisites[i]:
                res = self.depth_has_cycle(requisites, j, visited, visiting)
                if res:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]),True)
    print(Solution().canFinish(2, [[1, 0],[0,1]]), False)
