class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        j=0
        k=0
        while True:
            if j>=len(nums):
                break
            if nums[j]!=val:
                nums[i]=nums[j]
                i=i+1
                k=k+1
                j=j+1
            else:
                j=j+1
        return k