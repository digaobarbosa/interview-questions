#https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram("boi","iob"))
    print(s.isAnagram("aaab","aaba"))
    print(s.isAnagram("baba","aaba"))
