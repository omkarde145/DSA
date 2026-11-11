class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        if len(nums)>0:
            k=1
        else:
            k=0
        while True:
            if b==len(nums):
                break
            if nums[a]==nums[b]:
                b=b+1
            else:
                a=a+1
                nums[a]=nums[b]
                k=k+1
        return k