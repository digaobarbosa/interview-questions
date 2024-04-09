# https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=study-plan-v2&envId=top-interview-150
from typing import *

class SolutionLogn:

    def search_index(self,array:List[int],value:int,start:int,end:int)-> int:
        if len(array)==0:
            return 0
        p = start + (end-start)//2
        while start < p < end:
            if value < array[p]: # right position is to the left of p
                end = p
                p = start + (end-start)//2
            elif value >array[p]: # right position is to the right of p
                start = p
                p = start + (end-start)//2
            else:
                break
        return p if value <= array[p] else p+1



    def find_element_at(self,nums1:List,nums2:List,obj_index:int) -> int:
        start1,start2 = 0,0
        end1,end2 = len(nums1),len(nums2)
        p1 = start1 + (end1-start1)//2
        p2 = start2 + (end2-start2)//2
        double_median = (end1+end2) %2 ==0

        while start1 <= p1 < end1 or start2 <= p2 < end2 :
            if start1 <= p1 < end1:
                value1 = nums1[p1]
                index1 = self.search_index(nums2,value1,start2,end2)
                if index1 + p1 < obj_index:
                    start1 = p1
                    p1 = start1 + (end1-start1)//2
                elif index1 + p1 > obj_index:
                    end1 = p1
                    p1 = start1 + (end1-start1)//2
                else:
                    # print("p1=median=",p1, nums1[p1])
                    if not double_median:
                        return nums1[p1]
                    if len(nums1) > p1+1 and index1 < len(nums2) and nums1[p1+1] < nums2[index1]:
                        return (nums1[p1]+nums1[p1+1])/2
                    else:
                        return (nums1[p1]+nums2[index1-1])/2

            if start2 <= p2 < end2:
                value2 = nums2[p2]
                index2 = self.search_index(nums1,value2,start1,end1)
                if index2 + p2 < obj_index:
                    start2 = p2
                    p2 = start2 + (end2-start2)//2
                elif index2 + p2 > obj_index:
                    end2 = p2
                    p2 = start2 + (end2-start2)//2
                else:
                    # print("p2=median=",p2, nums2[p2])
                    if not double_median:
                        return nums2[p2]
                    if len(nums2) > p2+1 and index2 < len(nums1) and nums2[p2+1] < nums1[index2]:
                        return (nums2[p2]+nums2[p2+1])/2
                    else:
                        return (nums2[p2]+nums1[index2-1])/2

        # print("p1=",p1," p2=",p2)
        return nums1[p1]


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1,n2 = len(nums1), len(nums2)
        obj_median = (n1+n2)//2
        # print('obj =',obj_median)
        if (n1 + n2) %2 == 1:
            return self.find_element_at(nums1,nums2, obj_median)
        else:
            s = self.find_element_at(nums1,nums2, obj_median,)
            return s




class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = sorted(nums1 + nums2)
        if len(res) % 2 ==1:
            return res[len(res)//2]
        else:
            mid = len(res)//2
            return (res[mid] + res[mid-1])/2

if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1],[2]),1.5)
    print(Solution().findMedianSortedArrays([],[2]),2)
    print(Solution().findMedianSortedArrays([1],[]),1)
    print(Solution().findMedianSortedArrays([1,3],[2]),2)
    print(Solution().findMedianSortedArrays([1,2],[3,4]),2.5)
    print(Solution().findMedianSortedArrays([1,3],[2,4,5]),3)
    print(Solution().findMedianSortedArrays([1,3],[2,4]),2.5)
    print(Solution().findMedianSortedArrays([1,3],[2,4,5,6,7,8,9]),5)
    # print(Solution().findMedianSortedArrays([1,3],[2,4,5,6,7,8,9,10]),5.5)
