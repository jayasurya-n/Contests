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
            x,y,z = lii()
            adj[x-1].append((y-1,z))
            adj[y-1].append((x-1,z))
        
        def bfs(u,visited):
            q = deque([u])
            visited[u] = True
            comp = []
            
            while(q):
                u = q.popleft()
                comp.append(u)
                for v,w in adj[u]:
                    if(visited[v]):
                        if(val[v]==val[u]^w):continue
                        else:return [-1]
                    val[v] = val[u]^w
                    visited[v] = True
                    q.append(v)
            return comp

        val = [0]*n
        visited = [False]*n
        for u in range(n):
            if(visited[u]):continue
            val[u] = 0
            comp = bfs(u,visited)
            
            if(comp==[-1]):return [-1]
            
            for i in range(31):
                cnt1 = 0
                for j in comp:
                    if(val[j]&(1<<i)):cnt1+=1
                
                if(cnt1>len(comp)-cnt1):
                    for j in comp:val[j]^=(1<<i)
        
        return val


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(*ans)