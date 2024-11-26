# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from typing import *
def solution(N:int):
    # Implement your solution here
    s = str(N)
    if N < 0:# negative case
        for i in range(1,len(str(N))):
            d = int(s[i])
            if d > 5:
                if i == 0:
                    return int('5'+s)
                return int(s[0:i]+'5'+s[i:])
        return int(s+'5')
    else: # positive case
        for i in range(len(str(N))):
            d = int(s[i])
            if d < 5:
                if i == 0:
                    return int('5'+s)
                return int(s[0:i]+'5'+s[i:])
        return int(s+'5')


if __name__ == '__main__':
    print(solution(268))
    print(solution(670))
    print(solution(-999))
    print(solution(-9))
    print(solution(-1))