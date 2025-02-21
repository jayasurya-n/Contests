from typing import List,Optional
from collections import deque, defaultdict
import sys, heapq, bisect
from math import ceil, floor, gcd, sqrt, log

si = lambda: input().strip()
ii = lambda: int(si())
lsi = lambda: list(input().strip().split())
lii = lambda: list(map(int,input().strip().split()))

class Solution:
    def run(self):
        n,M = lii()
        prices = lii()
        
        def check(x):
            cnt = cost = 0
            for p in prices:
                j = (x+p)//(2*p)
                cnt+=j
                cost+=j*j*p
            return (cost,cnt)
        
        low = 0
        high = (2*(floor(sqrt(M/min(prices))))+1)*min(prices)

        while(low<=high):
            mid = (low+high)>>1
            if(check(mid)[0]<=M):low = mid+1
            else:high = mid-1
        
        return check(high)[1]+(M-check(high)[0])//low
        
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    for _ in range(1):
        ans = Solution().run()
        print(ans)