# https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        dx=[-1,1,0,0,-1,-1,1,1]
        dy=[0,0,1,-1,-1,1,-1,1]
        n=len(grid[0])
        m=len(grid)
        visited=[[0]*n for _ in range(m)]
        Q=deque()
        small=-1

        if grid[0][0]!=0 or grid[n-1][m-1]!=0:
            return -1
        
        Q.append((0,0,1))
        visited[0][0]=1

        while Q:
            x,y,length=Q.popleft()

            if x==n-1 and y==n-1:
                small=length
                break
            for i in range(8):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<n and 0<=yy<m and visited[xx][yy]==0 and grid[xx][yy]==0:
                    Q.append((xx,yy,length+1))
                    visited[xx][yy]=1

        return small