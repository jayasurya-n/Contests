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
        cost = lii()

        prefix = [0]*n
        prefix[0] = cost[0]
        for i in range(1,n):
            prefix[i] = min(prefix[i-1],cost[i])
        
        ans = min(cost[0],cost[n-1])
        for i in range(n-1,-1,-1):
            ans = min(ans,cost[i]+prefix[i-1])
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)