# https://leetcode.com/problems/network-delay-time/
import heapq
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph=defaultdict(list)
        for time in times:
            graph[time[0]].append((time[1],time[2]))

        cost={} # 비용
        pq=[] #우선순위 큐
        heapq.heappush(pq,(0,k)) # 시작 값 우선순위 큐에 push

        while pq:
            cur_cost, cur_val = heapq.heappop(pq) #우선순위 높은 데이터 pop
            if cur_val not in cost:
                cost[cur_val]=cur_cost #비용 업데이트
                for next_val,next_edge in graph[cur_val]:
                        next_cost = cur_cost + next_edge
                        heapq.heappush(pq,(next_cost,next_val))
        if len(cost)==n:
            return max(cost.values())
        return -1