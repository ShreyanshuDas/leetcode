class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        low = 1
        high = x
        res = 0
        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq < x:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res