class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        root = math.isqrt(num)
        return root * root == num
        