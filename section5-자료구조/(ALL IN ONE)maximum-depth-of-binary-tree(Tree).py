# https://leetcode.com/problems/maximum-depth-of-binary-tree/
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        max_dept=0
        if root is None:
            return max_dept
        Q=deque()
        Q.append((root, 1))
        while Q:
            now,cur_dept=Q.popleft()
            max_dept=max(max_dept,cur_dept)

            if now.left:
                Q.append((now.left,cur_dept+1))
            if now.right:
                Q.append((now.right,cur_dept+1))

        return max_dept
        