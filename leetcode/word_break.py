# https://leetcode.com/problems/word-break/description/?envType=study-plan-v2&envId=top-interview-150
from typing import *

""" I got this to practice some DP. Knowing it's a DP problem already helps solving a DP problem.

For this specific case, I think the problem can be broken down as:
1. For n > i > 0
2. solution(s) = any true (solution(s[0:i]) and solution(s[i:]) for every i)
3. We understand this will repeat a lot of calls for solutions.

Inside the solution we need to check:
if partial_s in wordDict return True
else any [solution(partial_s[:i] and solution(partial_s[i:] for i in range(len(partial_s))]


That would be a recursive solution, that probably would take a lot of time. Which we could memorize to help with speed and memory.

Thinking in a more DP approach for it, we can:
1. have a pointer that begins at the end of the string
2. Have a array with positions which the result is True
3. We only need to check if a combination of substrings between the pointer and other positions substrings is true

One might wonder. Is it sufficient to guarantee correctedness?
This could be rephrased as, is there a chance to build a True value even if the substring at the end is not valid?

Is it possible S is valid splitting at i, even if S[i:] is false? No

Complexity:
O(n)
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        valid_positions = []
        for ptr in range(len(s)-1,-1,-1):
            sub = s[ptr:]
            if sub in wordSet:
                valid_positions.append(ptr)
            else:
                for vpos in valid_positions:
                    subv = s[ptr:vpos]
                    if subv in wordSet:
                        valid_positions.append(ptr)
                        break
        return len(valid_positions)>0 and valid_positions[-1] == 0


if __name__ == '__main__':
    print(Solution().wordBreak('leetcode',["leet","code"]))
    print(Solution().wordBreak('applepenapple',["apple","pen"]))
    print(Solution().wordBreak('catsandog',["cats","dog","sand","and","cat"]))
    print(Solution().wordBreak('catsandog',["cats"]))
    print(Solution().wordBreak('c',["cats"]))
    print(Solution().wordBreak('c',["c"]))