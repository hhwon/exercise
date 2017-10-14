# -*- coding: utf-8 -*-
# __author__ = 'huang_wang'

"""
377 Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
"""


GCD = lambda a, b: (GCD(b, a % b) if a % b else b)

print(GCD(9, 3))