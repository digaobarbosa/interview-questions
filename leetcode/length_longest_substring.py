# https://leetcode.com/problems/longest-substring-without-repeating-characters/

from typing import *
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None or len(s) == 0: return 0
        counter: dict[str,int] = {s[0]:1}
        start = 0
        end = 1
        max_substring = 0
        while end < len(s):
            # print(f"start={start} end={end} counter={counter} sub={s[start:end]}")
            if counter.get(s[end],0) > 0:
                if start < end:
                    counter[s[start]] = counter[s[start]] -1
                    start += 1
                else:
                    counter[s[start]] = 0
                    start += 1
                    end += 1
            else:
                if end - start > max_substring:
                    max_substring = end - start
                    # print(s[start:end])
                # increment
                c = counter.get(s[end],0)
                counter[s[end]] = c + 1
                end += 1
        return max_substring+1

if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"),3)
    print(Solution().lengthOfLongestSubstring("bbbbb"),1)
    print(Solution().lengthOfLongestSubstring("qwerty"),6)

