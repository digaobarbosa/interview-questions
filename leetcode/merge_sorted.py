from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr = m + n - 1
        i1 = m - 1
        i2 = n - 1
        while i1 >= 0 or i2 >= 0:
            if i1 >= 0 and i2>=0:
                if nums1[i1] > nums2[i2]:
                    nums1[ptr] = nums1[i1]
                    i1 -= 1
                else:
                    nums1[ptr] = nums2[i2]
                    i2 -= 1
            elif i1>=0:
                nums1[ptr] = nums1[i1]
                i1 -= 1
            else:
                nums1[ptr] = nums2[i2]
                i2 -= 1
            ptr -= 1


if __name__ == '__main__':
    a1, a2 = [1, 2, 3, 0, 0, 0], [2, 5, 6]
    print(Solution().merge(a1, len(a1) - len(a2), a2, len(a2)))
    print(a1)

    a1, a2 = [1], []
    print(Solution().merge(a1, len(a1) - len(a2), a2, len(a2)))
    print(a1)
    a1, a2 = [0], [1]
    print(Solution().merge(a1, len(a1) - len(a2), a2, len(a2)))
    print(a1)

    a1, a2 = [-1,0,0,3,3,3,0,0,0], [1,2,2]
    print(Solution().merge(a1, len(a1) - len(a2), a2, len(a2)))
    print(a1)


