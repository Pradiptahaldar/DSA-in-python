class Solution(object):
    def factors(self, n):
        result = []

        i = 1
        while i * i <= n:
            if n % i == 0:
                result.append(i)

                if i != n // i:
                    result.append(n // i)

            i += 1

        result.sort()
        return result