# -*- coding: utf-8 -*-
# __author__ = 'huang_wang'

"""
Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range
"""


def range_bitwise_and(m, n):
    while m < n:
        n &= n-1
    return n


print(range_bitwise_and(0, 2147483647))
