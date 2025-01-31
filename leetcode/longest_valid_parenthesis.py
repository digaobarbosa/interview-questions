# https://leetcode.com/problems/longest-valid-parentheses/description/

import collections
from functools import lru_cache
from typing import *



class Solution:

    """
Using a stack to know which index is being closed when you see a ')'
    """
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if len(stack) ==0:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length



class Solution_sum:

    """
    )()()(()))

    (()()) [1 1 -1 1 -1 -1]
    )(
    """
    def longestValidParentheses(self, s: str) -> int:
        int_s = [c =='(' and 1 or -1 for c in s]
        max_length = 0
        start = s.find('(')
        if start < 0:
            return 0
        for i in range(start,len(s)):
            p_sum = 0
            for j in range(i,len(s)):
                p_sum += int_s[j]
                if p_sum < 0:
                    break
                if p_sum == 0 and j -i +1 > max_length:
                    max_length = j - i + 1
        return max_length





class SolutionBF:
    def longestValidParentheses(self, s: str) -> int:
        def check_maximum_length(i:int) -> int:
            count = 0
            max_length = 0
            j = i
            while j < len(s):
                c = s[j]
                if c == '(':
                    count += 1
                elif c == ')':
                    if count:
                        count -= 1
                    else:
                        return max_length
                if count == 0:
                    max_length = j-i+1
                j+=1
            return max_length

        m = 0
        for i in range(len(s)):
            m = max(m,check_maximum_length(i))
        return m



if __name__ == '__main__':
    print(Solution().longestValidParentheses("(()"),2)
    print(Solution().longestValidParentheses( ")()())"),4)
    print(Solution().longestValidParentheses( ")("),0)
    print(Solution().longestValidParentheses( ""),0)
    print(Solution().longestValidParentheses( "()))(("),2)
