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

        maxi = max([len(adj[u]) for u in range(n)])
        if(maxi<=2):return 2*n-1
        return n+1

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)