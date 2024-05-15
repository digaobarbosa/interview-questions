# https://leetcode.com/contest/weekly-contest-291/problems/remove-digit-from-number-to-maximize-result/

from typing import *

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_next = -1
        to_remove = -1
        for i in range(len(number)):
            c = number[i]
            if c == digit:
                nextd = 0
                if i < len(number) -1:
                    nextd = int(number[0:i]+number[i+1:])
                else:
                    nextd = int(number[0:-1])
                if nextd > max_next:
                    max_next = nextd
        return str(max_next)




if __name__ == '__main__':
    print(Solution().removeDigit('123','3'))
    print(Solution().removeDigit('1231','1'))
    print(Solution().removeDigit('551','5'))
    print(Solution().removeDigit('9515','5'))