# https://leetcode.com/problems/daily-temperatures/description/
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        output=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):
            while stack and stack[-1][1]<temperatures[i]:
                    output[stack[-1][0]]=i-stack[-1][0]
                    stack.pop()
            stack.append((i,temperatures[i]))
            
        return output
