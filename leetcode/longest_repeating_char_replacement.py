# https://leetcode.com/problems/longest-repeating-character-replacement/
import collections

class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        counter = collections.defaultdict(lambda: 0)
        res = 0
        maxf = 0
        for end in range(len(s)):
            counter[s[end]] += 1
            maxf = max(maxf,counter[s[end]])
            while end - start + 1 - maxf > k:
                counter[s[start]] -= 1
                start += 1
            res = max(res, end- start+1)
        return res



if __name__ == '__main__':
    # print(Solution().characterReplacement("ABAB",2),4)
    # print(Solution().characterReplacement("AABABB",1),4)
    # print(Solution().characterReplacement("BBBBB",1),5)
    # print(Solution().characterReplacement("ABCD",1),2)
    # print(Solution().characterReplacement("",1),0)
    # print(Solution().characterReplacement("ABCD",0),1)
    # print(Solution().characterReplacement("ABBCD",0),2)
    print(Solution().characterReplacement("AAAAABBBBCBB",4),10)
