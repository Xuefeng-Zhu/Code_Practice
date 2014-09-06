# You are climbing a stair case. It takes n steps to reach to the top

class Solution:
    # @param n, an integer
    # @return an integer
    cache = {}
    def climbStairs(self, n):
        if n <= 1:
            return 1
        else:
            result = self.cache.get(n)
            if result:
                return result
            else:
                result = self.climbStairs(n-1) + self.climbStairs(n-2)
                self.cache[n] = result
                return result
    