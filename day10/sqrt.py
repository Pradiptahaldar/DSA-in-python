#binary search approach
class Solution(object):
    def mySqrt(self, x):
        if x<2:
            return x
        start=1
        end=x
        while start<=end:
            mid =(start+end)//2
            if mid*mid ==x:
                return mid
            elif mid*mid<x:
                start=mid+1
            else:
                end=mid-1
        return end
#loiop approach
class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        i = 1
        while i * i <= x:
            i += 1
        return i - 1
#built in method
import math
class solution(object):
    def mySqrt(self, x):
        return int(math.sqrt(x))#not for leetcode