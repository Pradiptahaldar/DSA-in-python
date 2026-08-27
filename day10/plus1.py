#change to integer method
class Solution(object):
    def plusOne(self, digits):
        number = int(''.join(map(str, digits)))
        number += 1
        return list(map(int, str(number)))
#loop approach
class Solution(object): 
    def plusOne(self, digits): 
        for i in range(len(digits) - 1, -1, -1): 
            if digits[i] < 9: 
                digits[i] += 1 
                return digits 
            digits[i] = 0 
        return [1] + digits
#
