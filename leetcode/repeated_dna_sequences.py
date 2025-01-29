# https://leetcode.com/problems/repeated-dna-sequences/
from typing import *


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subs_map = {}
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub not in subs_map:
                subs_map[sub] = 1
            else:
                subs_map[sub] += 1
        return [k for k,v in subs_map.items() if v >1]





if __name__ == '__main__':
    print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"),["AAAAACCCCC","CCCCCAAAAA"])
    print(Solution().findRepeatedDnaSequences("AAAAAAAAAAA"),["AAAAAAAAAA"])