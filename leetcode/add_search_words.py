# https://leetcode.com/problems/design-add-and-search-words-data-structure/?envType=study-plan-v2&envId=top-interview-150
from typing import *
class WordDictionary:

    def __init__(self):
        self.children:Dict[chr,WordDictionary] = {}
        self.isWord = False


    def addWord(self, word: str) -> None:
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = WordDictionary()
            cur = cur.children[c]
        cur.isWord = True


    def search(self, word: str) -> bool:
        possible = [self]
        for c in word:
            if len(possible) == 0:
                return False
            if c == '.':
              new_possible = []
              for cur in possible:
                  new_possible.extend(cur.children.values())
              possible = new_possible
            else:
                new_possible = []
                for cur in possible:
                    if c in cur.children:
                        new_possible.append(cur.children[c])
                possible = new_possible

        return any(x.isWord for x in possible)


def test(calls, args):
    o = WordDictionary()
    for i in range(1, len(args)):
        c = calls[i]
        a = args[i]
        r = getattr(o, c)(*a)
        print(c+"("+str(a)+") = ",r)


if __name__ == '__main__':
    test(["WordDictionary","addWord","addWord","addWord","search","search","search","search"], [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]])
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)