# Given an integer array, find three numbers whose product is maximum and output the maximum product.
#
# Example 1:
#
# Input: [1,2,3]
# Output: 6
#
# Example 2:
#
# Input: [1,2,3,4]
# Output: 24
#
# Note:
#
#     The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
#     Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.


# 一种解决方案
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(nums) * max(a * b for a, b in [heapq.nsmallest(2, nums), heapq.nlargest(3, nums)[1:]])
