# https://leetcode.com/problems/word-ladder/
import string
from typing import *
from collections import Counter,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        size = len(beginWord)
        q = deque()
        q.append((1,beginWord))
        while q:
            count,w = q.popleft()
            if w == endWord:
                return count
            for i in range(size):
                for c in string.ascii_lowercase:
                    tmp = w[:i]+c+w[i+1:]
                    if tmp in words:
                        q.append((count+1,tmp))
                        words.remove(tmp)
        return 0

class Solution3:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        counter_cache:Dict[Any,bool] = dict()
        words = set(wordList)
        def dist1(w1:str,w2:str) -> bool:
            if counter_cache.get(w2):
                return False
            diff = False
            for i in range(len(w1)):
                if w1[i] !=w2[i]:
                    if not diff:
                        diff = True
                    elif diff:
                        return False
            counter_cache[w1] = True
            counter_cache[w2] = True
            return diff

        q = deque()
        q.append((0,beginWord))
        while q:
            count,w = q.popleft()
            if w == endWord:
                return count+1
            to_add = []
            for w2 in words:
                if w2 and dist1(w,w2):
                    to_add.append(w2)
                    q.append((count+1,w2))
            for e in to_add:
                words.remove(e)
        return 0
class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        counter_cache:Dict[Any,bool] = dict()
        def dist1(w1:str,w2:str) -> bool:
            diff = False
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    if not diff:
                        diff = True
                    elif diff:
                        diff = False
                        break
            return diff


        graph:Dict[str,List[str]] = dict()
        words = sorted([beginWord] + wordList)
        for w in words:
            graph[w] = []
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                w1 = words[i]
                w2 = words[j]
                if w1!=w2 and dist1(w1,w2):
                    graph[w1].append(w2)
                    graph[w2].append(w1)

        q = deque()
        q.append((0,beginWord))
        visited = {beginWord}
        while q:
            count,w = q.popleft()
            if w == endWord:
                return count+1
            for w2 in graph[w]:
                if w2 not in visited:
                    q.append((count+1,w2))
                    visited.add(w2)
        return 0


if __name__ == '__main__':
    print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
    print(Solution().ladderLength("hit","cog",["hot","dot","dog","lot","log"]))
    print(Solution().ladderLength("lost","miss",["most","mist","miss","lost","fist","fish"]))


