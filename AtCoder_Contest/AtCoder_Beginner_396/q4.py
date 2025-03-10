from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

def factorial(n,mod):
    fac = [1]*n
    for i in range(1,n):
        fac[i] = (fac[i-1]*i)%mod
    return fac

def nCr(n,r,fac,mod):
    if(n<r or n<0 or r<0):return 0
    return fac[n]*pow(fac[r],mod-2,mod)*pow(fac[n-r],mod-2,mod)

class Solution:
    def run(self):
        n,m = lii()
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = lii()
            adj[u-1].append((v-1,w))
            adj[v-1].append((u-1,w))
        
        def dfs(u,xor,visited):
            if(u==n-1):
                self.ans = min(self.ans,xor)
                return
        
            for v,w in adj[u]:
                if(visited[v]):continue
                visited[v] = True
                dfs(v,xor^w,visited)
                visited[v] = False
                
        self.ans = sys.maxsize
        visited = [False]*n
        visited[0] = True
        dfs(0,0,visited)
        return self.ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)