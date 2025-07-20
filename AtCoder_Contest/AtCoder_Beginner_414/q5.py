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
        mod = 998244353
        ans = (n*(n+1))//2

        # itearting through q values rather b beacuse q is O(2(n^0.5))
        # where as b is O(n) 
        b = 1
        while b<=n:
            q = n//b
            # this q will be the value from this b to n//q
            last = n//q
            ans+=mod-(last-b+1)*q
            ans%=mod
            b = last+1
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(1):
        ans = Solution().run()
        print(ans)