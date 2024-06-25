# https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150

from typing import *

class Trie:

    def __init__(self):
        self.children:Dict[chr,Trie] = {}
        self.isWord = False


    def insert(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isWord = True


    def search(self, word: str) -> bool:
        cur = self
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.isWord


    def startsWith(self, prefix: str) -> bool:
        cur = self
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True



def test(calls, args):
    o = Trie()
    for i in range(1, len(args)):
        c = calls[i]
        a = args[i]
        r = getattr(o, c)(*a)
        print(c+"("+str(a)+") = ",r)

if __name__ == '__main__':
    print(test(["Trie", "insert", "search", "search", "startsWith", "insert", "search"],[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]))
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)