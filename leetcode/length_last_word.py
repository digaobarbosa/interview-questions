# https://leetcode.com/problems/length-of-last-word/?envType=study-plan-v2&envId=top-interview-150

from typing import *

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])



if __name__ == '__main__':
    print(Solution().lengthOfLastWord("Hello World"))