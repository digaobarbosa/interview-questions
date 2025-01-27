# https://leetcode.com/problems/count-and-say/
from typing import *

class SolutionRecursive:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            s = self.countAndSay(n-1)
            res = ''
            countprev = 1
            prev = s[0]
            for c in s[1:]:
                if c != prev:
                    res = res + (str(countprev)+prev)
                    countprev = 1
                    prev = c
                else:
                    countprev += 1
            res = res + (str(countprev)+prev)
            return res

class Solution:
    def encoding(self,s:str) -> str:
        res = ''
        countprev = 1
        prev = s[0]
        for c in s[1:]:
            if c != prev:
                res = res + (str(countprev)+prev)
                countprev = 1
                prev = c
            else:
                countprev += 1
        res = res + (str(countprev)+prev)
        return res

    def countAndSay(self, n: int) -> str:
        s = "1"
        i = 1
        while i < n:
            s = self.encoding(s)
            i += 1
        return s




if __name__ == '__main__':
    print(Solution().countAndSay(1),1)
    print(Solution().countAndSay(2),11)
    print(Solution().countAndSay(3),21)