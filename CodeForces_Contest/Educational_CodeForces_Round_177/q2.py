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
        n,k,x = lii()
        arr = lii()
        suffix = [0]*n
        suffix[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            suffix[i] = suffix[i+1]+arr[i]
        
        tsum = suffix[0]
        mini = 10**12
        for i in range(n-1,-1,-1):
            d = ceil((x-suffix[i])/tsum)
            mini = min(mini,d*n+n-i-1)
        return n*k-min(n*k,mini)
            
if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)