import numpy as np

class ProductOfNumbers(object):

    def __init__(self):
        self.prefix = [1]

    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1] * num)

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """
        # num = len(self.data) - k
        
        # return np.prod(self.data[num:])
        if k >= len(self.prefix):
            return 0
        
        return self.prefix[-1] // self.prefix[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))