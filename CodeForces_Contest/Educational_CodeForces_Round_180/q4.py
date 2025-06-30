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
        degree = [0]*n
        for _ in range(n-1):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
            degree[u-1]+=1
            degree[v-1]+=1
        
        root = None
        for u in range(n):
            if(degree[u]==2):
                root = u
                break
        
        if root is None:
            print(no) 
            return

        @bootstrap
        def dfs(u,par,color):
            if(color==1):ans.append((u,par))
            else:ans.append((par,u))

            for v in adj[u]:
                if(v==par):continue
                yield dfs(v,u,-color)
            yield          
        
        ans = []
        dfs(adj[root][0],root,1)
        dfs(adj[root][1],root,-1)

        print(yes)
        for u,v in ans:
            print(u+1,v+1)



if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()