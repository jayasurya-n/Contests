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

        ans = []
        pmin = [10**7]*n
        for i in range(n):
            pmin[i] = min(arr[i],pmin[i-1] if i>0 else 10**7)

        smax = [-10**7]*n
        for i in range(n-1,-1,-1):
            smax[i] = max(arr[i],smax[i+1] if i<n-1 else -10**7)

        ans = []
        for i in range(n):
            if(arr[i]==pmin[i] or arr[i]==smax[i]):
                ans.append('1')
            else:ans.append('0')
        
        return "".join(ans)

if __name__ == "__main__":
    # fac = factorial(n=2*(10**5)+5,mod=10**9+7)
    # yes,no = "YES","NO"
    # seed = random.randint(0,10**9+7)
    for _ in range(ii()):
        ans = Solution().run()
        print(ans)