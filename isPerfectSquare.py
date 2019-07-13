class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if((num ** .5) % 1 == 0):
            return True
        else:
            return False
