class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_of_squre(x):
            return sum(int(digit) ** 2 for digit in str(x))
        while n != 1 and n != 4:
            n = sum_of_squre(n)
        return n == 1

        