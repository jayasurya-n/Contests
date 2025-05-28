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
        n = ii()
        danger = lii()
        adj = [[] for _ in range(n)]

        for _ in range(n-1):
            u,v = lii()
            u-=1
            v-=1
            adj[u].append(v)
            adj[v].append(u)
        
        parent = [None]*n
        parent[0] = -1

        bfs = []
        q = deque([0])

        while q:
            u = q.popleft()
            bfs.append(u)
            for v in adj[u]:
                if(parent[v]!=None):continue
                parent[v] = u
                q.append(v)
        
        dp = [0]*n
        dp[0] = danger[0]

        for i in range(1,n):
            u = bfs[i]
            par = parent[u]
            par_par = parent[par]
            dp[u] = max(danger[u],
                       danger[u]-danger[par]+(dp[par_par] if par_par!=-1 else 0)) 
            
        return dp
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)