# https://leetcode.com/problems/minimum-window-substring/?envType=study-plan-v2&envId=top-interview-150
from typing import *
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        chars = set(t)
        analyze_array = [(i,s[i],None) for i in range(len(s)) if s[i] in chars]
        char_dict = defaultdict(int)
        for c in t:
            char_dict[c]+=1
        minimum_length = len(s)
        minimum_tuple = (None,None)
        for i in range(len(analyze_array)):
            copy_chars = char_dict.copy()
            start,chi,_ = analyze_array[i]
            for j in range(i,len(analyze_array)):
                end,ch,_ = analyze_array[j]
                chc = copy_chars.get(ch)
                if chc is None:
                    continue
                else:
                    copy_chars[ch] -= 1
                    if copy_chars[ch] ==0:
                        copy_chars.pop(ch)
                    if len(copy_chars)==0:
                        if end-start < minimum_length:
                            minimum_tuple = (start,end+1)
                            minimum_length = end-start
                            break
                    elif end - start >=minimum_length:
                        break
        if minimum_tuple[0] is not None:
            return s[minimum_tuple[0]:minimum_tuple[1]]
        return ""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        chars = set(t)
        char_dict = defaultdict(int)
        for c in t:
            char_dict[c]+=1
        minimum_length = len(s)
        start = 0
        end = 0
        count = 0
        result_start = 0
        result_end = 0
        while end < len(s):
            if s[end] not in chars:
                end +=1
                continue
            chi = s[end]
            counter = char_dict[chi]
            if counter > 0:
                count+=1
            char_dict[chi]-=1

            if count == len(t):
                j = start
                while char_dict[s[j]] < 0 or s[j] not in chars:
                    chj = s[j]
                    char_dict[chj] += 1
                    j += 1
                start = j
                if end - start < minimum_length:
                    start = j
                    minimum_length = end - start
            end += 1

        if count == len(t):
            return s[start:start+minimum_length+1]
        return ""

if __name__ == '__main__':
    print(Solution().minWindow("ADOBECODEBANC","ABC"),"BANC")
    print(Solution().minWindow("A","A"),"A")
    print(Solution().minWindow("ABCD","ABC"),"ABC")
    print(Solution().minWindow("DBCA","ABC"),"BCA")
    print(Solution().minWindow("A","AA"),"empty")
    print(Solution().minWindow("ADOBECODEBANC","AA"),"ADOBECODEBA")
    print(Solution().minWindow("ADOBECODEBANC","Z"),"empty")

