from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n,m = lii()
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = lii()
            adj[u-1].append((v-1,w))
            adj[v-1].append((u-1,w))

        def dijkstras(adj,start):
            dis = [10**10]*n
            dis[start] = 0
            pq = [(0,start)]

            while pq:
                d,u = heapq.heappop(pq)
                if(d>dis[u]):continue
                for v,w in adj[u]:
                    if(dis[v]>max(d,w)):
                        dis[v] = max(d,w)
                        heapq.heappush(pq,(dis[v],v))
            return dis

        d1 = dijkstras(adj,0)        
        d2 = dijkstras(adj,n-1)
        ans = 10**10
        for u in range(n):
            for v,w in adj[u]:
                ans = min(ans,w+max(d1[u],d2[v],w))
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)