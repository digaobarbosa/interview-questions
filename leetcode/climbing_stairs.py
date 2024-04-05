from typing import *
mem = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        elif mem.get(str(n)) is not None:
            return mem.get(str(n))
        else:
            v = self.climbStairs(n-1) + self.climbStairs(n-2)
            mem[str(n)] = v
            return v


if __name__ == '__main__':
    '''
    n=2
    out=2
    
    n=3
    out=3
    
    for n=4
    1 1 1 1
    1 1 2
    1 2 1
    2 1 1
    2 2
    out=5
    
    for n=5
    1 1 1 1 1
    1 1 1 2
    1 1 2 1
    1 2 1 1
    2 1 1 1
    1 2 2
    2 1 2
    2 2 1
    out=8
    
    for n=6
    1 1 1 1 1 1
    1 1 1 1 2
    1 1 1 2 1
    1 1 2 1 1
    1 2 1 1 1
    2 1 1 1 1
    1 1 2 2
    1 2 1 2
    1 2 2 1
    2 1 1 2
    2 1 2 1
    2 2 1 1
    2 2 2
    '''
