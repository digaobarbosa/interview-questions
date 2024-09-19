# https://leetcode.com/problems/permutation-in-string/description/

import collections

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = collections.Counter(s1)
        counter2 = collections.defaultdict(lambda: 0)

        start = 0
        for end in range(len(s2)):
            c2 = s2[end]
            counter2[c2] += 1
            if c2 not in counter1:
                start = end + 1
                counter2 = collections.defaultdict(lambda: 0)
            elif counter2[c2] > counter1[c2]:
                while s2[start] != c2:
                    counter2[s2[start]] -= 1
                    start = start + 1
                counter2[s2[start]] -= 1
                start = start + 1
            if counter2[c2] == counter1.get(c2,0) and (end - start + 1) == len(s1):
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion("ab","eidbaooo"),True)
    print(Solution().checkInclusion("ab","eidboaoo"),False)
    print(Solution().checkInclusion("a","abc"),True)
    print(Solution().checkInclusion("bc","abc"),True)
    print(Solution().checkInclusion("abc","cbad"),True)
    print(Solution().checkInclusion("adc","dcda"),True)
    print(Solution().checkInclusion("d","abc"),False)
