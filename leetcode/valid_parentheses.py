# https://leetcode.com/problems/valid-parentheses/description/
from typing import *
class Solution:
    def isValid(self, s: str) -> bool:
        brackets_close = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []
        for c in s:
            if c in brackets_close.keys():
                open_bracket = brackets_close[c]
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last != open_bracket:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0



if __name__ == '__main__':
    print(Solution().isValid("()"),"True")
    print(Solution().isValid("()]"),"False")
    print(Solution().isValid("[()]"),"True")
    print(Solution().isValid("[(])"),"False")