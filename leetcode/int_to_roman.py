#https://leetcode.com/problems/integer-to-roman/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class Solution:
    def intToRoman(self, num: int) -> str:
        iNumbers = [1000,100,10,1]
        rNumbers = ['M','C','X','I']

        ivNumbers=[0,500,50,5]
        rvNumbers=['?','D','L','V']

        res = ''

        for i in range(4):
            N = num // iNumbers[i]
            num = num % iNumbers[i]
            if iNumbers[i]==1000 or N <= 3:
                res += rNumbers[i]*N
            elif N==9:
                res += rNumbers[i]+rNumbers[i-1]
            elif N==4:
                res += rNumbers[i]+rvNumbers[i]
            else:
                res += rvNumbers[i] + (rNumbers[i]*(N-5))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(10),'X')
    print(s.intToRoman(9),'IX')
    print(s.intToRoman(2),'II')
    print(s.intToRoman(20),'XX')
    print(s.intToRoman(4),'IV')
    print(s.intToRoman(58),'LVIII')
    print(s.intToRoman(1994),'MCMXCIV')




