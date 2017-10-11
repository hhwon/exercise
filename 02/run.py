# -*- coding: utf-8 -*-


class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        new_queue = []
        for _ in range(len(self.queue) - 1):
            new_queue.append(self.queue.pop(0))
        res = self.queue.pop()
        self.queue = new_queue
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        new_queue = []
        for _ in range(len(self.queue) - 1):
            new_queue.append(self.queue.pop(0))
        res = self.queue.pop()
        new_queue.append(res)
        self.queue = new_queue
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.queue

        # Your MyStack object will be instantiated and called as such:
        # obj = MyStack()
        # obj.push(x)
        # param_2 = obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.empty()
