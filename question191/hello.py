# Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
#
# For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.


# 一种解决方案
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')


# 另外一种解决方案
def hammingWeight(self, n):
    """
    :type n: int
    :rtype: int
    """
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c
