class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        rev_str = str(abs(x))[::-1]
        rev_int = int(rev_str) * sign
        if -2**31 <= rev_int <= 2**31-1:
            return rev_int
        else:
            return 0

        