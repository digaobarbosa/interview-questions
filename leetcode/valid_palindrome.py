# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join([c for c in s if c.isalnum()])
        for i in range(len(s)//2):
            if s[i] != s[-1-i]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("arara_,,,..."),True)
    print(Solution().isPalindrome("ararab"),False)
    print(Solution().isPalindrome("aabaa"),True)
    print(Solution().isPalindrome("aaaa"),True)