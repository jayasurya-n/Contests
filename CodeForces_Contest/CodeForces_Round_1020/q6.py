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
        self.zeros = [0]*(n+1)
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
            self.zeros[rootv]+=self.zeros[rootu]
        else:
            self.parent[rootv] = rootu
            self.size[rootu]+=size_v
            self.zeros[rootu]+=self.zeros[rootv]
            
            
class Solution:
    def run(self):
        n = ii()
        s = si()
        
        ds = DisjointSet(3*n)
        for i in range(n):
            base = 3*i
            if(s[i]=='0'):
                ds.zeros[base] = i
                ds.zeros[base+1] = 0
                ds.zeros[base+2] = n-i-1
            else:
                ds.zeros[base] = 0
                ds.zeros[base+1] = 1
                ds.zeros[base+2] = 0
        
        
        for i in range(1,n):
            if(s[i]=='0' and s[i-1]=='0'):
                ds.unionbySize(3*(i-1),3*i)
                ds.unionbySize(3*(i-1)+2,3*i+2)
            elif(s[i]=='0' and s[i-1]=='1'):
                ds.unionbySize(3*(i-1)+1,3*i)
            elif(s[i]=='1' and s[i-1]=='0'):
                ds.unionbySize(3*(i-1)+2,3*i+1)
            
        
        ans = 0
        for i in range(3*n):
            if(ds.findUltimateParent(i)==i):
                ans = max(ans,ds.zeros[i])
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)