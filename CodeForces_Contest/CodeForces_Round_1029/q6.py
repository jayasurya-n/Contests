from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args,**kwargs):
        if stack:return f(*args,**kwargs)
        else:
            to = f(*args,**kwargs)
            while True:
                if isinstance(to, GeneratorType):
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

class Solution:
    def run(self):
        n = ii()
        adj = [[] for _ in range(n)]
        mod = 10**9+7

        for _ in range(n-1):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        
        @bootstrap
        def dfs(u,par,d):
            if(len(adj[u])>2):self.h_lca = d
            leaf = True
            for v in adj[u]:
                if(v==par):continue
                yield dfs(v,u,d+1)
                leaf = False
            if(leaf):self.leafs.append(d)
            yield

        self.h_lca = None
        self.leafs = []
        adj[0].append(-1)
        dfs(0,-1,1)

        if(len(self.leafs)>2):return 0
        elif(len(self.leafs)==1):return pow(2,n,mod)
        
        diff = abs(self.leafs[0]-self.leafs[1])
        if(diff==0):return pow(2,self.h_lca+1,mod)
        return (pow(2,self.h_lca+diff,mod)+pow(2,self.h_lca+diff-1,mod))%mod

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)