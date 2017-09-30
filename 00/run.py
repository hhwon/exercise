# -*- coding: utf-8 -*-
# __author__ = 'huang_wang'
# 求解第n个默尼森数

import math


def prime(n):
    try:
        i = 2
        while i <= math.sqrt(n):
            if n % i == 0:
                return False
            i += 1
        return n
    except ValueError:
        return False


def sen(n):
    if prime(2**n-1) and prime(n):
        return prime(2**n-1)
    else:
        return False


def ca(n):
    i = 1
    p = 2
    m = False
    while i <= n:
        m = sen(p)
        if m:
            i += 1
        p += 1
    return m


if __name__ == '__main__':
    num = 8
    print(ca(num))
