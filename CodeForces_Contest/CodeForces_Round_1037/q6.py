import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

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
        n,q = lii()
        colors = lii()
        adj = [[] for _ in range(n)]

        hash = [defaultdict(int) for _ in range(n)]

        ans = 0
        for _ in range(n-1):
            u,v,c = lii()
            adj[u-1].append((v-1,c))
            adj[v-1].append((u-1,c))
            if(colors[u-1]!=colors[v-1]):ans+=c

        @bootstrap
        def dfs(u,par,w):
            parents[u] = [par,w]
            for v,c in adj[u]:
                if(v==par):continue
                hash[u][colors[v]^seed]+=c
                yield dfs(v,u,c)
            yield

        parents = [0]*n
        dfs(0,-1,None)

        for _ in range(q):
            u,new = lii()
            u-=1

            if(colors[u]==new):
                print(ans)
                continue
            
            old = colors[u]
            colors[u] = new
            ans+=hash[u][old^seed]
            ans-=hash[u][new^seed]

            if(u!=0):
                par,w = parents[u] 
                if(old!=colors[par]):ans-=w
                if(new!=colors[par]):ans+=w

                hash[par][old^seed]-=w
                hash[par][new^seed]+=w

            print(ans)
        

if __name__ == "__main__":
    # yes,no = "YES","NO"
    seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()