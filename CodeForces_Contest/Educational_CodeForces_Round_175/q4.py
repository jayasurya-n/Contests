from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n = ii()
        arr = lii()
        
        adj = [[] for _ in range(n)]
        level = [-1]*n
        level[0] = 0
        for i in range(n-1):
            v = i+1
            parent = arr[i]-1
            adj[parent].append(v)
            adj[v].append(parent)
            level[v] = level[parent]+1
        
        dp = [0]*n
        dp[0] = 1
        q = deque([])
        for v in adj[0]:q.append(v)
        prevTotal = 2

        while q:
            curTotal = 0
            for _ in range(len(q)):
                u = q.popleft()
                for v in adj[u]:
                    if(level[v]==level[u]-1):
                        dp[u] = prevTotal-dp[v]
                        dp[u]%=mod
                    elif(level[v]==level[u]+1):q.append(v)
                curTotal+=dp[u]
                curTotal%=mod
            prevTotal = curTotal
        
        ans = 0
        for i in range(n):
            ans+=dp[i]
            ans%=mod
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    mod = 998244353
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)