# -*- coding: utf-8 -*-
# __author__ = 'huang_wang'

import numpy as np


class Integrate(object):

    def __init__(self):
        self.x = np.array([2, 4])   # x的积分域
        self.y = np.array([1, 2])   # y的积分域
        self.w_g = np.array([25/81, 40/81, 25/81, 40/81, 64/81, 40/81, 25/81, 40/81, 25/81])
        # 高斯点权值这里采用三点积分
        a = np.sqrt(3/5)
        self.g_x = np.array([-a, 0, a, -a, 0, a, -a, 0, a])
        self.g_y = np.array([a, a, a, 0, 0, 0, -a, -a, -a])
        self.xi = np.array([])
        self.yi = np.array([])
        self.ans = 0

    def cor(self):
        self.xi = (self.x[1]-self.x[0])/2*self.g_x+(self.x[0]+self.x[1])/2
        self.yi = (self.y[1]-self.y[0])/2*self.g_y+(self.y[1]+self.y[0])/2

    def integrate(self):
        self.ans = (self.x[1]-self.x[0])/2*(self.y[1]-self.y[0])/2*self.w_g.dot(self.xi*self.yi)   # f=xy


nn = Integrate()
nn.cor()
nn.integrate()
print(nn.ans)
