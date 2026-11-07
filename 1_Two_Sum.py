class Solution(object):
    def twoSum(self, nums, target):
        val={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in val:
                return[val[diff],i]
            val[n]=i
   