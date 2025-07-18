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
        arr.sort()

        if(arr[n-2]+arr[n-3]>arr[n-1]):return arr[n-1]
        ans = arr[n-2]

        for k in range(n-1):
            for j in range(n-2,k,-1):
                csum = arr[j]+arr[k] 
                ans = max(ans,arr[n-1]%csum)
        return ans

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)