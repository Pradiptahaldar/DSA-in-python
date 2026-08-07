class Solution(object):
    def isArmstrong(self, n):
        """
        :type n: int
        :rtype: bool
        """
        original = n
        total = 0
        nod = len(str(n))

        while n > 0:
            last_digit = n % 10
            total += last_digit ** nod
            n //= 10

        return total == original