class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                lst.append(i)
            elif len(lst)==0:
                return False
            elif i==')':
                if lst[-1]=='(':
                    lst.pop()
                else:
                    return False
            elif i=='}':
                if lst[-1]=='{':
                    lst.pop()
                else:
                    return False
            elif i==']':
                if lst[-1]=='[':
                    lst.pop()
                else:
                    return False
        if len(lst)==0:
            return True
        else:
            return False