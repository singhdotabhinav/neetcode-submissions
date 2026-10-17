class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        res = [0] * (n + 1)
        res[1] = 1
        res[2] = 2
        for each in range(3, n + 1):
            res[each] = res[each-1] + res[each-2]
        return res[n]
