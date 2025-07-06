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
        n,q = lii()
        b = lii()
        queries = []
        for _ in range(q):
            x,y,z = lii()
            queries.append((x-1,y-1,z-1))
        
        temp = b.copy()

        for i in range(q-1,-1,-1):
            x,y,z = queries[i]
            val = temp[z]
            temp[z] = -1
            temp[x] = max(temp[x],val)
            temp[y] = max(temp[y],val)
        
        for i in range(n):
            if(temp[i]==-1):temp[i] = b[i]

        a = temp.copy()

        for i in range(q):
            x,y,z = queries[i]
            temp[z] = min(temp[x],temp[y])
        
        if(temp==b):return a
        return [-1]


if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*ans)