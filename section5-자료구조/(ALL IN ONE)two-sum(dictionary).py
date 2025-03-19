# https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}

        for idx,val in enumerate(nums):
            if (target-val) in hash :
                return [hash[target-val],idx]
            else:
                hash[val]=idx