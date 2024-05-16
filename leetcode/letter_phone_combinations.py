# https://leetcode.com/problems/letter-combinations-of-a-phone-number/?envType=study-plan-v2&envId=top-interview-150
from typing import *


class Solution:
    letter_map = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }


    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = ['']
        for d in digits:
            temp_result = []
            for subs in result:
                for c in Solution.letter_map[d]:
                    temp_result.append(subs+c)
            result = temp_result
        return result


if __name__ == '__main__':
    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations("2"))
