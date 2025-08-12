import math, heapq, bisect, random, sys
from collections import deque, defaultdict

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))
modinv = lambda a,mod:pow(a,mod-2,mod)

class Solution:
    def run(self):
        n = ii()
        adj = [[] for _ in range(n)]
        degree = [0]*n

        for _ in range(n-1):
            u,v = lii()
            u-=1
            v-=1
            adj[u].append(v)
            adj[v].append(u)
            degree[u]+=1
            degree[v]+=1
        
        if(n==2):return 0
        leafs = 0
        maxi = 0
        for u in range(n):
            if(degree[u]==1):leafs+=1
            cnt = 0
            for v in adj[u]:
                if(degree[v]==1):cnt+=1
            maxi = max(maxi,cnt)
        
        return leafs-maxi


if __name__ == "__main__":
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)