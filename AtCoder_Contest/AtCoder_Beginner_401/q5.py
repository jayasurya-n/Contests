from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class DisjointSet:
    def __init__(self,n):
        self.rank = [0]*(n+1)
        self.parent = list(range(n+1))

    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbyRank(self,u,v):
        rootu = self.findUltimateParent(u)
        rootv = self.findUltimateParent(v)
        if(rootu==rootv):return False

        rank_u = self.rank[rootu]
        rank_v = self.rank[rootv]

        if(rank_u < rank_v):self.parent[rootu] = rootv
        elif(rank_u > rank_v):self.parent[rootv] = rootu
        else:
            self.parent[rootv] = rootu
            self.rank[rootu]+=1
        
        return True

class Solution:
    def run(self):
        n,m = lii()
        adj = [[] for _ in range(n)]
        for _ in range(m):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        ds = DisjointSet(n)
        
        comp = cnt = 0
        borders = [False]*n
        
        for k in range(0,n):
            comp+=1
            for v in adj[k]:
                if(v<k and ds.unionbyRank(k,v)):comp-=1
            
            if(borders[k]):
                borders[k] = False
                cnt-=1
            
            for v in adj[k]:
                if(v>k and borders[v]==False):
                    borders[v] = True
                    cnt+=1
            
            if(comp==1):print(cnt)
            else:print(-1)
        

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()