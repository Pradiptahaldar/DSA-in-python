from bisect import bisect_left
class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []
        for num in nums:
            i = bisect_left(tails, num)
            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num
        return len(tails)