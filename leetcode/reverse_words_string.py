# https://leetcode.com/problems/reverse-words-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))