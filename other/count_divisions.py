from typing import *
def solution2(S:str):
    # Implement your solution here
    V = int(S,base=2)
    count = 0
    while V > 0:
        if V % 2 == 0:
            V = V // 2
        else:
            V = V -1
        count += 1
    return count

def solution(S:str):
    # Implement your solution here
    V = int(S,base=2)
    s = '{:b}'.format(V)
    count = 0
    for i in range(len(s)-1,-1,-1):
        if s[i]=='1':
            count += 2
        else:
            count +=1
    return count-1



if __name__ == '__main__':
    print(solution('1'),solution2('1'))
    print(solution('10'),solution2('10'))
    print(solution('11'),3)
    print(solution('100'),solution('100'))
    print(solution('101'),5)
    print(solution('110'),solution2('110'))
    print(solution('111'),solution2('111'))
    print(solution('1000'),8)
    print(solution('011100'),solution2('011100'))
    print(solution('1111010101111'))