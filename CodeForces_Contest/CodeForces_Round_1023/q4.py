from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect, random
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))


class Solution:
    def run(self):
        n = ii()
        adj = [[] for _ in range(n)]

        for _ in range(n-1):
            u,v = lii()
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)

       
        def diameter_(u):
            def longest_path(u,par):
                q = deque([(1,u,par)])
                max_d,max_node = 1,u 
                while q:
                    d,u,par = q.popleft()
                    parent[u] = par
                    if(max_d<d):
                        max_d = d
                        max_node = u
                    elif(d==max_d):
                        max_node = max(max_node,u)
                
                    for v in adj[u]:
                        if(v==par or removed[v]):continue
                        q.append((d+1,v,u))
                return max_d,max_node
            
            d,end1 = longest_path(u,-1)
            d,end2 = longest_path(end1,-1)
            return d,end1,end2

        ans = []
        q = deque([])
        parent = [-1]*n
        removed = [False]*n

        d,st,end = diameter_(0)
        ans.append([d,max(st,end)+1,min(st,end)+1])
        dia = []
        while(end!=-1):
            removed[end] = True
            dia.append(end)
            end = parent[end]

        for u in dia:
            for v in adj[u]:
                if(removed[v]):continue
                q.append(v)    
        
        while q:
            u = q.popleft()
            if(removed[u]):continue
            d,st,end = diameter_(u)
            ans.append([d,max(st,end)+1,min(st,end)+1])
            dia = []
            while(end!=-1):
                removed[end] = True
                dia.append(end)
                end = parent[end]

            for u in dia:
                for v in adj[u]:
                    if(removed[v]):continue
                    q.append(v) 

        ans.sort(reverse=True)
        return [ele for row in ans for ele in row]

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)