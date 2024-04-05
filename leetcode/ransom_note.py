# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *
from collections import defaultdict

def init_counter():
    return 0

class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = defaultdict(init_counter)
        for c in magazine:
            count = counter[c]
            counter[c] = count+1
        for c in ransomNote:
            count = counter[c]
            if count >0:
                counter[c] = count-1
            else:
                return False
        return True


if __name__ == '__main__':
    Solution().canConstruct("abc","abcdefgabc")