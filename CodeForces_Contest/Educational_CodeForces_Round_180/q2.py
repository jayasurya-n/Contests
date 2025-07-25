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

        for i in range(n-1):
            if(abs(arr[i]-arr[i+1])<=1):return 0
        
        ok = False
        for i in range(1,n-1):
            if(min(arr[i-1],arr[i])<=arr[i+1]<=max(arr[i-1],arr[i])):
                ok = True
                break

            if(min(arr[i+1],arr[i])<=arr[i-1]<=max(arr[i+1],arr[i])):
                ok = True
                break

        return 1 if ok else -1

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)