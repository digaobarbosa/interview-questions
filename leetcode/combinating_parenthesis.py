#https://leetcode.com/problems/generate-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
import itertools
from typing import *


class Solution:

    def _recStr(self, ss: str, a: int, f: int, cur_open: int, res: List[str]) -> str:
        if a + f == 0:
            res.append(ss)
            return ss
        if a > 0:
            self._recStr(ss + '(', a - 1, f, cur_open + 1, res)
        if f > 0 and cur_open > 0:
            self._recStr(ss + ')', a, f - 1, cur_open - 1, res)
        return ''

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self._recStr('',n,n,0, res)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1), ['()'])
    print(s.generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])
