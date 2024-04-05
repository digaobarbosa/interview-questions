# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
import random
from typing import *


class RandomizedSet:

    def __init__(self):
        self.list = []
        self.set = dict()  # has value as key, and points to list index

    def insert(self, val: int) -> bool:
        if val not in self.set:
            self.set[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        index = self.set.get(val)
        if index is None:
            return False
        self.list[index] = None
        self.set.pop(val)
        return True

    def getRandom(self) -> int:
        i = random.randrange(0, len(self.list))
        while self.list[i] is None:
            i = random.randrange(0, len(self.list))
        return self.list[i]


if __name__ == '__main2__':
    s = RandomizedSet()
    s.insert(0)
    s.insert(1)
    s.remove(0)
    s.insert(2)
    s.remove(1)
    print(s.getRandom())

if __name__ == '__main__':
    s = RandomizedSet()
    s.insert(0)
    s.insert(1)
    s.insert(2)
    s.insert(3)
    s.insert(4)
    s.remove(0)
    s.remove(1)
    print([s.getRandom() for i in range(10)])
