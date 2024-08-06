# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import *


class Solution:
    def topKFrequent(self, nums: List[int], K: int) -> List[int]:
        table = dict()
        for n in nums:
            count = table.get(n, 0)
            table[n] = count + 1

        # build frequency list
        freq = [[] for r in range(len(nums)+1)]
        for k,v in table.items():
            freq[v].append(k)
        topK = []
        for i in range(len(nums),0,-1):
            topK.extend(freq[i])
            if len(topK) >= K:
                return topK
        return topK


if __name__ == '__main__':
    print(Solution().topKFrequent([1,1,1,2,2,3],2),"[1,2]")
    print(Solution().topKFrequent([1],1),"[1]")


