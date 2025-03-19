# https://leetcode.com/problems/longest-consecutive-sequence/
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash={}
        big=0

        for i in nums:
            if i not in hash:
                hash[i]=True

        for i in hash:
            if i-1 not in hash:
                cnt=1
                target=i+1
                while target in hash:
                    target+=1
                    cnt+=1
                big=max(big,cnt)
        return big
