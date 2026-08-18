#noted
class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)

        expected_sum = n * (n + 1) // 2

        actual_sum = sum(nums)

        return expected_sum - actual_sum
#another way
class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        for i in range (len(nums)):
            if nums[i]!= i:
                return i
        return len(nums)