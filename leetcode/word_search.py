# https://leetcode.com/problems/word-search/

from typing import *
import heapq
from collections import Counter

class Solution_iter:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_count = Counter([c for l in board for c in l])
        word_count = Counter(word)
        for k,v in word_count.items():
            if v > board_count.get(k,0):
                return False

        used = set()
        Q = [(0,i,j,set()) for j in range(len(board[0])) for i in range(len(board))]
        heapq.heapify(Q)
        while Q:

            pos,i,j,used = heapq.heappop(Q)
            pos = -pos
            if i < 0 or i >= len(board) or j < 0 or j>= len(board[0]) or (i,j) in used:
                continue
            if word[pos] == board[i][j]:
                if pos == len(word)-1:
                    return True
                used = used.copy()
                used.add((i,j))
                heapq.heappush(Q,(-pos-1,i-1,j,used))
                heapq.heappush(Q,(-pos-1,i+1,j,used))
                heapq.heappush(Q,(-pos-1,i,j-1,used))
                heapq.heappush(Q,(-pos-1,i,j+1,used))
        return False


class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_count = Counter([c for l in board for c in l])
        word_count = Counter(word)
        for k,v in word_count.items():
            if v > board_count.get(k,0):
                return False
        def dfs(i,j,pos,used):
            if i < 0 or i >= len(board) or j < 0 or j>= len(board[0]) or (i,j) in used:
                return False
            if word[pos] == board[i][j]:
                used.add((i,j))
                if pos == len(word)-1:
                    return True
                res = (dfs(i+1,j,pos+1,used) or
                    dfs(i-1,j,pos+1,used) or 
                    dfs(i,j-1,pos+1,used) or
                    dfs(i,j+1,pos+1,used) )
                used.remove((i,j))
                return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                res = dfs(i,j,0,set())
                if res:
                    return True
        return False
        
    
s = Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))    
print(s.exist([["a","b"],["c","d"]],"acdb"))
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))
                



        

