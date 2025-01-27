# https://leetcode.com/problems/interleaving-string/

from typing import *

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = dict()
        def is_interleave(i1:int,i2:int,i3:int):
            key = (i1,i2,i3)
            if key in cache:
                return cache[key]
            if i1 == len(s1):
                if i2 < len(s2) and i3 < len(s3):
                    r = s2[i2:] == s3[i3:]
                    cache[key] = r
                    return r
            if i2 == len(s2):
                if i1 < len(s1) and i3 < len(s3):
                    r = s1[i1:] == s3[i3:]
                    cache[key] = r
                    return r
            if i1 >= len(s1) or i2 >= len(s2) or i3 >= len(s3):
                return False
            result = False
            if i1 < len(s1) and i3 < len(s3) and s1[i1] == s3[i3]:
                result = is_interleave(i1+1,i2,i3+1)
            if not result and i2 < len(s2) and i3 < len(s3) and s2[i2] == s3[i3]:
                result = is_interleave(i1,i2+1,i3+1)
            cache[key] = result
            return result
        return len(s3+s2+s1)==0 or is_interleave(0,0,0)


if __name__ == '__main__':
    print(Solution().isInterleave("aa","bb","aabb"))
    print(Solution().isInterleave("aa","bb","abab"))
    print(Solution().isInterleave("aa","bb","ababb"))
    print(Solution().isInterleave("","",""))
    print(Solution().isInterleave("aabcc","dbbca","aadbbcbcac"))
