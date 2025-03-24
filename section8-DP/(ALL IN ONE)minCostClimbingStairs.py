# https://leetcode.com/problems/min-cost-climbing-stairs/
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # bottom-up(반복문)
        cost.append(0)
        memo={0:cost[0],1:cost[1]}
        for i in range(2,len(cost)):
            memo[i]=cost[i]+min(memo[i-1],memo[i-2])
        return memo[len(cost)-1]
        