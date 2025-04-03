from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
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
        n = ii()
        adj = [set() for _ in range(n)]
        for _ in range(n-1):
            u,v = lii()
            adj[u-1].add(v-1)
            adj[v-1].add(u-1)
        
        def dfs(u,d,levels):
            levels[u] = d
            for v in adj[u]:
                if(levels[v]!=-1):continue
                dfs(v,d+1,levels)
        
        levels = [-1]*n
        dfs(0,0,levels)
        
        hash = set()
        
        for i in range(n):
            l1 = levels[i]
            for j in range(i+1,n):
                l2 = levels[j]
                if((l2-l1)%2==1 and (j not in adj[i])):
                    hash.add((i,j))
        
        if(len(hash)%2==1):
            print("First")
            sys.stdout.flush()
        else:
            print("Second")
            sys.stdout.flush()
            x,y = lii()
            hash.remove((x-1,y-1))

        while True:
            mx,my = hash.pop() 
            print(mx+1,my+1)
            sys.stdout.flush()
            x,y = lii()
            if(x==-1 and y==-1):return
            else:hash.remove((x-1,y-1))
                

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()