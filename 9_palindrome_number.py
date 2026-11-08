class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        b=0
        c=0
        a=x
        while(a>0):
            b=a%10
            c=c*10+b
            a=a//10
        if c==x:
            return True
        else:
            return False