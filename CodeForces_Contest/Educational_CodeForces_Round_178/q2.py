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
        arr = lii()
        
        pmax = [0]*(n+1)
        for i in range(1,n+1):
            pmax[i] = max(pmax[i-1],arr[i-1])
        
        ans = []
        csum = 0
        for k in range(1,n+1):
            csum+=arr[n-k]
            if(arr[n-k]<pmax[n-k]):ans.append(csum-arr[n-k]+pmax[n-k])
            else:ans.append(csum)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(*
              ans)