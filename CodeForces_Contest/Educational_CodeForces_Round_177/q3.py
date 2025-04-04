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
        self.size = [1]*(n+1)
        self.parent = list(range(n+1))

    def findUltimateParent(self,u):
        if(u==self.parent[u]):return u
        self.parent[u] = self.findUltimateParent(self.parent[u])
        return self.parent[u]

    def unionbySize(self,u,v):
        rootu = self.findUltimateParent(u)
        rootv = self.findUltimateParent(v)
        if(rootu==rootv):return

        size_u = self.size[rootu]
        size_v = self.size[rootv]

        if(size_u < size_v):
            self.parent[rootu] = rootv
            self.size[rootv]+=size_u
        else:
            self.parent[rootv] = rootu
            self.size[rootu]+=size_v

class Solution:
    def run(self):
        n = ii()
        p = lii()
        d = lii()
        
        ds = DisjointSet(n)
        for i in range(n):
            ds.unionbySize(i+1,p[i])
        
        ans = []
        cnt = 0
        hash = [0]*n
        for i in range(n):
            parent = ds.findUltimateParent(d[i])
            if(hash[parent-1]==0):
                cnt+=ds.size[parent]
                hash[parent-1] = 1
            ans.append(cnt)
        return ans
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)