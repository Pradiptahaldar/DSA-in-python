class Solution(object):
    def moveZeroes(self, nums):
        position = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[position] = nums[i]
                position += 1

        while position < len(nums):
            nums[position] = 0
            position += 1